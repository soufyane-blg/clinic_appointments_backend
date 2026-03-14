from rest_framework import serializers
from datetime import date

from .models import Appointment, AppointmentNote


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = "__all__"

    def validate(self, data):

        start_time = data.get("start_time")
        end_time = data.get("end_time")
        appointment_date = data.get("date")

        
        if start_time and end_time:
            if start_time >= end_time:
                raise serializers.ValidationError(
                    "End time must be after start time"
                )

        
        if appointment_date:
            if appointment_date < date.today():
                raise serializers.ValidationError(
                    "Cannot create appointment in the past"
                )

        
        if self.instance:
            if self.instance.status in ["COMPLETED", "CANCELLED"]:
                raise serializers.ValidationError(
                    "Completed or cancelled appointments cannot be modified"
                )

        return data


class AppointmentNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentNote
        fields = "__all__"


class TimeSlotSerializer(serializers.Serializer):
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()