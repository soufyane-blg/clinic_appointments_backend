from rest_framework import serializers
from .models import Appointment, AppointmentNote


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class AppointmentNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentNote
        fields = "__all__"