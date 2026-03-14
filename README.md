# Clinic Appointment Management API

A RESTful API for managing clinic appointments with time-slot scheduling, 
conflict prevention, and role-based access control.

Built with Django and Django REST Framework.

---

## Features

- JWT Authentication
- Appointment scheduling system
- Time slot generation
- Conflict prevention (no overlapping appointments)
- Appointment cancellation and rescheduling
- Available slots API
- Filtering and pagination
- Role-based access (admin / staff / doctor)

---

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication

---

## API Examples

Authentication:

POST /api/token/
POST /api/token/refresh/

Appointments:

GET  /api/appointments/appointments/
POST /api/appointments/appointments/
POST /api/appointments/appointments/{id}/cancel/
POST /api/appointments/appointments/{id}/reschedule/

Available slots:

GET /api/appointments/available-slots/?doctor_id=1&date=2026-04-10

---

## Run the Project

git clone 
cd clinic-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## Author

Backend project for learning API design and scheduling systems with Django REST Framework.

