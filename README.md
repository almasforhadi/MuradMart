# 🛒 E-Shop — Django E-commerce Platform

A modern **Django-based E-commerce web application** featuring product browsing, cart management, order processing, and secure online payments via **SSLCommerz**.
The project is containerized using **Docker** and served with **Gunicorn**, making it ready for deployment on platforms like **Render**.

---

# 🚀 Features

### 🛍️ Shopping Experience

* Product listing with categories
* Product detail page
* Product rating and reviews
* Product search and filtering

### 🛒 Cart System

* Add to cart
* Update cart quantity
* Remove items
* Session-based cart for guests
* Persistent cart for logged-in users

### 💳 Checkout & Orders

* Cash on Delivery (COD)
* Secure online payment with **SSLCommerz**
* Order confirmation system
* Order status tracking

### 👤 User Accounts

* User registration and login
* Google social login (via **Django Allauth**)
* Profile management
* Password change

### ⭐ Product Ratings

* Only users who purchased a product can rate it
* Star rating (1-5)
* Review comments

### 📧 Email Notifications

* Order confirmation email sent after successful order placement

---

# 🏗️ Tech Stack

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Django         | Backend web framework         |
| Gunicorn       | Production WSGI server        |
| Docker         | Containerization              |
| SQLite         | Database (development)        |
| Django Allauth | Authentication & Google Login |
| SSLCommerz     | Online payment gateway        |
| WhiteNoise     | Static file serving           |
| Bootstrap      | Frontend UI                   |
| Crispy Forms   | Form rendering                |

---

# 📂 Project Structure

```
eshop/
│
├── eshop/                # Django project settings
├── shop/                 # Main ecommerce application
│
├── static/               # Static assets (css/js/images)
├── media/                # Uploaded images
├── staticfiles/          # Collected static files
│
├── templates/            # HTML templates
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── manage.py
```

---

# ⚙️ Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your_secret_key
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

# SSLCommerz
SSLCOMMERZ_STORE_ID=your_store_id
SSLCOMMERZ_STORE_PASSWORD=your_store_password
SSLCOMMERZ_PAYMENT_URL=https://sandbox.sslcommerz.com/gwprocess/v4/api.php
SSLCOMMERZ_VALIDATION_URL=https://sandbox.sslcommerz.com/validator/api/validationserverAPI.php

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

---

# 🐳 Running with Docker

### 1️⃣ Build containers

```bash
docker compose build
```

### 2️⃣ Run containers

```bash
docker compose up
```

### 3️⃣ Open the app

```
http://localhost:8000
```

---

# 🔧 Local Development (Without Docker)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Run development server

```bash
python manage.py runserver
```

---

# 💳 Payment Integration

This project integrates **SSLCommerz** payment gateway.

Supported payment methods:

* Credit / Debit Cards
* Mobile Banking (bKash, Nagad, Rocket)
* Internet Banking

Payment flow:

```
Checkout
   ↓
SSLCommerz Payment Gateway
   ↓
Payment Verification
   ↓
Order Confirmation
```

---

# 📦 Deployment

The project can be deployed easily using **Render**.

Deployment flow:

```
Local Development
      ↓
Git Push → GitHub
      ↓
Render Auto Deploy
      ↓
Live Production Server
```

Whenever new code is pushed to GitHub, **Render automatically redeploys the application**.

---

# 🔐 Security Features

* CSRF protection
* Secure session cookies
* XSS protection
* Content-type sniffing prevention
* Payment verification with SSLCommerz

---

# 🧪 Admin Panel

Django Admin allows management of:

* Products
* Categories
* Orders
* Users
* Ratings

Admin URL:

```
/admin
```

---

# 📸 Future Improvements

Possible enhancements:

* PostgreSQL database
* Redis caching
* Order tracking dashboard
* Wishlist feature
* Product recommendation system
* REST API (Django REST Framework)
* Celery for background tasks

---

# 👨‍💻 Author

Developed as a **full-stack Django e-commerce project** demonstrating:

* Backend architecture
* Payment integration
* Docker deployment
* Production-ready configuration

---

# 📄 License

This project is open-source and available for learning and educational purposes.
