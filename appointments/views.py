from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appointment, AppointmentNote
from .serializers import AppointmentSerializer, AppointmentNoteSerializer
from doctors.models import DoctorProfile

from core.permissions import IsAdmin, IsStaff, IsDoctorOwnerOfAppointment

from .services import create_appointment, is_slot_available

from django_filters.rest_framework import DjangoFilterBackend


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsStaff]

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "doctor",
        "patient",
        "date",
        "status"
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Appointment.objects.all()

        if hasattr(user, "doctorprofile"):
            return Appointment.objects.filter(doctor=user.doctorprofile)

        return Appointment.objects.none()

    def perform_create(self, serializer):

        doctor = serializer.validated_data["doctor"]
        patient = serializer.validated_data["patient"]
        date = serializer.validated_data["date"]
        start_time = serializer.validated_data["start_time"]
        end_time = serializer.validated_data["end_time"]

        try:
            appointment = create_appointment(
                doctor=doctor,
                patient=patient,
                date=date,
                start_time=start_time,
                end_time=end_time,
                created_by=self.request.user
            )

        except ValueError as e:
            raise ValidationError(str(e))

        serializer.instance = appointment

    # Cancel appointment
    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        appointment = self.get_object()

        if appointment.status == "CANCELLED":
            raise ValidationError("Appointment already cancelled")

        appointment.status = "CANCELLED"
        appointment.save()

        return Response({"detail": "Appointment cancelled successfully"})

    # Reschedule appointment
    @action(detail=True, methods=["post"])
    def reschedule(self, request, pk=None):

        appointment = self.get_object()

        date = request.data.get("date")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")

        if not date or not start_time or not end_time:
            raise ValidationError("date, start_time and end_time are required")

        if not is_slot_available(
            doctor=appointment.doctor,
            date=date,
            start_time=start_time,
            end_time=end_time
        ):
            raise ValidationError("This time slot is already booked")

        appointment.date = date
        appointment.start_time = start_time
        appointment.end_time = end_time
        appointment.save()

        return Response({"detail": "Appointment rescheduled successfully"})


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


# -------- Available Slots API --------

class AvailableSlotsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        doctor_id = request.query_params.get("doctor")
        date = request.query_params.get("date")
        start_time = request.query_params.get("start_time")
        end_time = request.query_params.get("end_time")

        if not doctor_id or not date or not start_time or not end_time:
            raise ValidationError(
                "doctor, date, start_time and end_time are required"
            )

        doctor = DoctorProfile.objects.get(id=doctor_id)

        available = is_slot_available(
            doctor=doctor,
            date=date,
            start_time=start_time,
            end_time=end_time
        )

        return Response({
            "doctor": doctor_id,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "available": available
        })