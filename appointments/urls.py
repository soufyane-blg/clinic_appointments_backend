from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AppointmentViewSet,
    AppointmentNoteViewSet,
    AvailableSlotsView
)

router = DefaultRouter()

router.register(
    r'appointments',
    AppointmentViewSet,
    basename='appointments'
)

router.register(
    r'appointment-notes',
    AppointmentNoteViewSet,
    basename='appointment-notes'
)

urlpatterns = [
    path('', include(router.urls)),

    # Available slots endpoint
    path(
        'available-slots/',
        AvailableSlotsView.as_view(),
        name='available-slots'
    ),
]