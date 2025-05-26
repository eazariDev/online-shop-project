# payment/views.py

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from orders.models import Order
import stripe

from .tasks import payment_completed_notification

from shop.models import Product
from shop.recommender import Recommender


# stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version=settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == "POST":
        success_url = request.build_absolute_uri(
            reverse("payment:completed")
        )
        cancel_url = request.build_absolute_uri(
            reverse("payment:canceled")
        )
        
        session_data = {
            "mode": "payment",
            "client_reference_id": order.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": []
        }
        
        # adding order items to the stripe checkout session
        for item in order.items.all():
            session_data["line_items"].append(
                { 
                "price_data": {
                    "unit_amount": int(item.price * Decimal('100')),
                    "currency": "usd",
                    "product_data": {
                        "name": item.product.name,
                    },
                },
                "quantity": item.quantity,
                }
            )
            
            # add coupon to stripe
            if order.coupon:
                stripe_coupon = stripe.Coupon.create(
                    name=order.coupon.code,
                    percent_off=order.discount,
                    duration='once'
                )
                session_data['discounts'] = [{'coupon': stripe_coupon.id}]
        
        # stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        
        #redirect to stripe payment form
        return redirect(session.url, code=303)

    else:
        return render(
            request, "payment/process.html", locals()
        )
        
        
def payment_completed(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    order.paid = True
    order.save()
    request.session['coupon_id'] = None
    
    #save items bought for product recommendation
    product_ids = order.items.values_list('product_id')
    products = Product.objects.filter(id__in=product_ids)
    r = Recommender()
    r.products_bought(products)
    
    
    # launch celery task
    payment_completed_notification.delay(order.id)
    return render(request, "payment/completed.html")
    
def payment_canceled(request):
    return render(request, "payment/canceled.html")
    