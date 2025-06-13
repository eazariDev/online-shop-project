<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="logo.png" width="30%" align="left" style="margin-right: 20px">

<br />
<br />
<h1> ONLINE-SHOP-PROJECT </h1>
<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/eazariDev/online-shop-project?style=plastic&logo=opensourceinitiative&logoColor=white&color=blueviolet" alt="license">
<img src="https://img.shields.io/github/last-commit/eazariDev/online-shop-project?style=plastic&logo=git&logoColor=white&color=blueviolet" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/eazariDev/online-shop-project?style=plastic&color=blueviolet" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/eazariDev/online-shop-project?style=plastic&color=blueviolet" alt="repo-language-count">


<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Django-blue?style=plastic&logo=django&logoColor=white" alt="Django">
<img src="https://img.shields.io/badge/SQLite-blue?style=plastic&logo=sqlite&logoColor=white" alt="Sqlite">
<img src="https://img.shields.io/badge/Git-F05032?style=plastic&logo=sqlite&logoColor=white" alt="Sqlite">



<br clear="left"/>

## ☀️ Table of Contents

1. [☀ ️ Table of Contents](#-table-of-contents)
2. [🌞 Overview](#-overview)
3. [⚙️ Tech Stack](#-Tech-Stack)
4. [🔥 Features](#-features)
5. [🌅 Project Structure](#-project-structure)
6. [🚀 Getting Started](#-getting-started)
7. [🤝 Contributing](#-contributing)

---

## 🌞 Overview

The Online Shop Project is a Django-based web application for an e-commerce platform. It provides the core functionalities required to manage an online shop, including cart management, order processing, payment integration, and coupon handling. The project follows the Model-View-Controller (MVC) architecture and is modular, allowing for easy scalability and the addition of new features.


---

## ⚙️ Tech Stack
* Backend Framework: Django
* Programming Language: Python
* Database: SQLite (default), can be configured for PostgreSQL or MySQL
* Authentication: Django's built-in user authentication system
* Payment Gateway: Custom integration with a Stripe payment gateway
* Frontend: HTML, CSS (via Django templates), basic static files
* Development Tools:
  * Package Manager: pip
  * Version Control: Git (GitHub repository)
  * IDE/Editor: Visual Studio Code, PyCharm (or any Python-compatible editor)
  * Virtual Environment: venv or virtualenv for dependency management

---

## 🔥 Features

* User Authentication: Supports basic user login and registration.

* Shopping Cart: Add, remove, and update products in the cart.

* Order Management: Create, process, and view orders.

* Payment Integration: Secure payment gateway for transaction processing.

* Coupons: Apply discount coupons for users.

* Admin Dashboard: Admin interface to manage products, orders, and payments.

|     | Component         | Details                                                                                                                                                                                                        |
| :-- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Django-based architecture for the online shop</li><li>Modular with apps such as cart, orders, and payment</li><li>Uses model-view-controller (MVC) pattern</li></ul>                                   |
| 🔩  | **Code Quality**  | <ul><li>Separation of concerns with apps for each functionality</li><li>Well-structured models, views, and templates</li><li>Tests provided for key components (cart, orders, payment)</li></ul>               |
| 🔌  | **Integrations**  | <ul><li>Payment integration with external service (model and views for payment processing)</li><li>Coupon functionality for discounts</li></ul>                                                                |
| 🧩  | **Modularity**    | <ul><li>Decoupled apps for cart, coupons, orders, and payment</li><li>Flexible for adding new features like user authentication or product reviews</li></ul>                                                   |
| ⚡️  | **Performance**   | <ul><li>Basic database optimizations for common queries</li><li>Potential performance gains with caching and database indexing</li></ul>                                                                       |
| 🛡️ | **Security**      | <ul><li>Security features provided by Django (user authentication, CSRF protection)</li><li>Payment handling must be securely integrated with an external service</li></ul>                                    |
| 📦  | **Dependencies**  | <ul><li>Django</li><li>External payment gateway library</li><li>Unit test libraries</li></ul>                                                                                                                  |
| 🚀  | **Scalability**   | <ul><li>Modular structure allows for easy scaling (e.g., adding more payment methods, new product categories)</li><li>Can scale horizontally with Django's ability to deploy across multiple servers</li></ul> |

---

## 🌅 Project Structure
The project is organized into several Django apps, each responsible for a specific functionality:

- cart: Manages the shopping cart, including adding, removing, and updating products.

- coupons: Handles coupon codes and discounts for users.

- orders: Manages the order creation, order processing, and order history.

- payment: Integrates with external payment gateways to process payments.

- shop: Handles the product catalog, recommendations, and shop-specific functionalities.

- static: Contains the static files (CSS, images, etc.).

- media: Stores uploaded files (such as product images).

```sh
└── online-shop-project/
    ├── cart
    ├── coupons
    ├── manage.py
    ├── media
    │   └── products
    ├── myshop
    ├── orders
    ├── payment
    ├── shop
    └── static
        ├── admin
        ├── css
        └── img
```


## 🚀 Getting Started

### 🌟 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python

### ⚡ Installation

Build online-shop-project from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/eazariDev/online-shop-project
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd online-shop-project
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    
4. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://github.com/eazariDev/online-shop-project/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eazariDev/online-shop-project/issues)**: Submit bugs found or log feature requests for the `online-shop-project` project.
- **💡 [Submit Pull Requests](https://github.com/eazariDev/online-shop-project/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eazariDev/online-shop-project
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/eazariDev/online-shop-project/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eazariDev/online-shop-project">
   </a>
</p>
</details>

---
