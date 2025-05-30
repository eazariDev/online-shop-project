import os

from celery import Celery


# set the default django settings module for the cleery program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")

app = Celery("myshop")
app.config_from_object("django.conf.settings", namespace="CELERY")
app.autodiscover_tasks()

