# 🏨 StayNest API — Smart Hotel Booking Platform

StayNest API is a production-ready **Hotel Booking Backend** built with Django and Django REST Framework.
It provides secure JWT authentication, hotel & room management, booking workflow, wallet transactions, and fully documented APIs via Swagger and Redoc.

---

## 🚀 Key Features

✅ Custom User Model (Email Login)
✅ JWT Authentication with Djoser
✅ Hotel & Room Management
✅ Booking System with Validation
✅ Wallet System with Transactions
✅ Reviews & Ratings
✅ API Documentation (Swagger + Redoc)
✅ Cloud Image Storage (Cloudinary)
✅ PostgreSQL Production Database
✅ Role-based Permissions
✅ Nested API Routes

---

## 🧱 Tech Stack

* Python 3.13
* Django
* Django REST Framework
* PostgreSQL
* Djoser (JWT Auth)
* drf_yasg (Swagger Docs)
* Cloudinary (Media Storage)
* WhiteNoise (Static Files)
* django-filter

---

## 📂 Project Structure

```
hotel_booking/
│
├── api/
├── users/
├── hotels/
├── rooms/
├── bookings/
├── wallet/
├── fixtures/
│   └── sample_data.json
│
├── hotel_booking/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
└── manage.py
```

---

## ⚙️ Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/staynest-api.git
cd staynest-api
```

### 2️⃣ Create virtual environment

```bash
python -m venv .hotel_env
.hotel_env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Create `.env` file:

```
dbname=your_db
user=your_user
password=your_password
host=localhost
port=5432

cloud_name=xxxx
cloudinary_api_key=xxxx
api_secret=xxxx
```

### 5️⃣ Run migrations

```bash
python manage.py migrate
```

### 6️⃣ Load sample data (optional)

```bash
python manage.py loaddata fixtures/sample_data.json
```

### 7️⃣ Run server

```bash
python manage.py runserver
```

---

## 🔐 Authentication Flow

### Register

```
POST /auth/users/
```

```json
{
  "email": "user@example.com",
  "password": "password123",
  "re_password": "password123"
}
```

### Get JWT Token

```
POST /auth/jwt/create/
```

### Use token

```
Authorization: JWT <access_token>
```

---

## 📡 Main API Endpoints

### 👤 Users

| Method | Endpoint            | Description        |
| ------ | ------------------- | ------------------ |
| GET    | /api/v1/users/      | List users (Admin) |
| GET    | /api/v1/users/{id}/ | Profile            |
| PATCH  | /api/v1/users/{id}/ | Update             |

---

### 🏨 Hotels

| Method | Endpoint             |
| ------ | -------------------- |
| GET    | /api/v1/hotels/      |
| POST   | /api/v1/hotels/      |
| GET    | /api/v1/hotels/{id}/ |

---

### 🛏 Rooms

| Method | Endpoint            |
| ------ | ------------------- |
| GET    | /api/v1/rooms/      |
| POST   | /api/v1/rooms/      |
| GET    | /api/v1/rooms/{id}/ |

---

### 📅 Bookings

| Method | Endpoint               |
| ------ | ---------------------- |
| GET    | /api/v1/bookings/      |
| POST   | /api/v1/bookings/      |
| PATCH  | /api/v1/bookings/{id}/ |
| DELETE | /api/v1/bookings/{id}/ |

---

### 💰 Wallet

| Method | Endpoint                           |
| ------ | ---------------------------------- |
| GET    | /api/v1/wallets/                   |
| GET    | /api/v1/wallets/{id}/transactions/ |

---

## 📚 API Documentation

### Swagger UI

```
http://127.0.0.1:8000/swagger/
```

### Redoc

```
http://127.0.0.1:8000/redoc/
```

---

## 🧪 Testing with Sample Data

```
python manage.py loaddata fixtures/sample_data.json
```

Includes:

* Hotels
* Rooms
* Users
* Wallets
* Bookings
* Reviews

---

## 🔒 Permissions

👤 User can:

* Book rooms
* View own wallet
* Add reviews

👑 Admin can:

* Manage all data
* View all bookings
* Manage users

---

## ☁️ Media Storage

Cloudinary is used for storing:

* Hotel images
* Room images

---

## 🛠 Deployment

Production ready with:

✅ PostgreSQL
✅ WhiteNoise
✅ Cloudinary
✅ Environment variables

---

## 🐛 Common Issues

### Swagger not loading

✔ Ensure DEBUG=True locally
✔ Check drf_yasg installed
✔ Verify static files

### JWT not working

✔ Use header:

```
Authorization: JWT <token>
```

---

## 👨‍💻 Author

Sakir Mohammad Safayet

---

## 📜 License

MIT License

---

## ⭐ Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 💡 Future Improvements

* Payment gateway integration
* Email notifications
* Booking calendar UI
* Rate limiting
* Docker support

---

⭐ If you like this project, give it a star on GitHub!
