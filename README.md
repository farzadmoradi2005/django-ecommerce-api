# E-Commerce REST API

A comprehensive backend RESTful API for an E-Commerce platform built with **Django** and **Django REST Framework (DRF)**. This project features relational data modeling (Categories, Products, Carts, Orders), transactional business logic (inventory tracking during checkout), JWT authentication, and automated test coverage.

## 🚀 Features

* **JWT Authentication:** Secure user registration and token management via `djangorestframework-simplejwt`.
* **Product Catalog:** Product and category management with search, filtering, and pagination.
* **Shopping Cart System:** User-specific cart management allowing addition, quantity updates, and deletion of items.
* **Order & Checkout Logic:** Dynamic transaction system that converts cart items into confirmed orders and automatically updates product inventory stock.
* **Custom Permissions:** Strict access controls for admin users (catalog management) vs authenticated customers (cart and order management).
* **Automated Unit Testing:** Test suite built with DRF's `APITestCase` to verify core business logic and API safety.

## 🛠️ Tech Stack

* **Language:** Python 3.12+
* **Framework:** Django 5.x
* **API Toolkit:** Django REST Framework (DRF)
* **Authentication:** SimpleJWT
* **Database:** SQLite (Development)

## ⚙️ Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/farzadmoradi2005/django-ecommerce-api.git
   cd django-ecommerce-api
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## 📡 Core API Reference

| Section | Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- | :--- |
| **Auth** | `POST` | `/api/auth/register/` | Register new user account | Public |
| **Auth** | `POST` | `/api/auth/token/` | Obtain Access/Refresh tokens | Public |
| **Products** | `GET` | `/api/products/` | List products with filters/search | Public |
| **Products** | `GET` | `/api/products/{id}/` | Get details of a single product | Public |
| **Cart** | `GET` | `/api/cart/` | View current user's cart | Authenticated |
| **Cart** | `POST` | `/api/cart/items/` | Add item to shopping cart | Authenticated |
| **Orders** | `POST` | `/api/checkout/` | Convert cart to order & update stock | Authenticated |
| **Orders** | `GET` | `/api/orders/` | View user's order history | Authenticated |
