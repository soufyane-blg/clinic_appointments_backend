from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Appointment, AppointmentNote
from .serializers import AppointmentSerializer, AppointmentNoteSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentNoteViewSet(viewsets.ModelViewSet):
    queryset = AppointmentNote.objects.all()
    serializer_class = AppointmentNoteSerializer
    permission_classes = [IsAuthenticated]