# Clinic Appointment Management API

A RESTful API for managing clinic appointments with time-slot scheduling, conflict prevention, and role-based access control.

Built with Django and Django REST Framework.

---

## Key Highlights

- Designed a scheduling system with conflict prevention
- Implemented a service layer for business logic separation
- Built a time-slot availability engine
- Role-based access control for different user types

---

## Features

- JWT Authentication
- Doctor profiles and working hours
- Appointment scheduling system
- Conflict prevention (no overlapping appointments)
- Appointment rescheduling and cancellation
- Available slots API
- Role-based access control
- Interactive API documentation (Swagger)

---

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication
- OpenAPI / Swagger (drf-spectacular)

---

## Architecture

The project follows a layered architecture:

Client  
↓  
Views (API endpoints)  
↓  
Serializers (data validation)  
↓  
Services (business logic)  
↓  
Models (database)

Core logic such as appointment scheduling and conflict detection is implemented in the service layer.

---

## Main API Endpoints

Authentication  
POST /api/token/  
POST /api/token/refresh/

Appointments  
GET  /api/appointments/appointments/  
POST /api/appointments/appointments/  
POST /api/appointments/appointments/{id}/cancel/  
POST /api/appointments/appointments/{id}/reschedule/

Available slots  
GET /api/appointments/available-slots/?doctor=1&date=2026-04-10&start_time=10:00&end_time=10:30

---

## API Documentation

Swagger UI available at:

http://127.0.0.1:8000/api/docs/

---

## Run the Project

git clone <repo_url>  
cd clinic-api  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver

---

## Author

Backend project for learning API design and scheduling systems with Django REST Framework.