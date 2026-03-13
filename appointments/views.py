from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Appointment, AppointmentNote
from .serializers import AppointmentSerializer, AppointmentNoteSerializer

from core.permissions import IsAdmin, IsStaff, IsDoctorOwnerOfAppointment


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsStaff]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Appointment.objects.all()

        return Appointment.objects.none()

    def perform_create(self, serializer):
        serializer.save()


class AppointmentNoteViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentNoteSerializer
    permission_classes = [
        IsAuthenticated,
        IsDoctorOwnerOfAppointment | IsAdmin | IsStaff
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return AppointmentNote.objects.all()

        return AppointmentNote.objects.filter(
            appointment__doctor=user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)