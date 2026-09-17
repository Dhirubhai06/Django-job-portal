# Django-job-portal
A Django-based Job Portal web application that allows users to view and manage job listings, with a Python backend, database integration, and a simple web interface.

# Django Job Portal

A web-based **Job Portal application** built using Python and Django. The project allows users to view available job opportunities through a simple and user-friendly interface.

## 🚀 Features

* View available job listings
* Display job details
* Django-based backend
* Database integration using Django ORM
* Responsive web interface
* Admin panel for managing job information

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **SQLite**
* **Django ORM**
* **Git & GitHub**

## 📂 Project Structure

```text
django-job-portal/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── job/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── ...
│
└── static/
    └── ...
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Open the project

```bash
cd YOUR_REPOSITORY
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 👨‍💻 Author

**Dhiru Aranya**

B.Tech – Artificial Intelligence & Data Science

## 📌 Future Improvements

* User registration and login
* Job search and filtering
* Job application functionality
* Company profiles
* Email notifications
* REST API integration

## 📄 License

This project is created for **learning and educational purposes**.
