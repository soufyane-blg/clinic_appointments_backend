from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, AppointmentNoteViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'appointment-notes', AppointmentNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]