from rest_framework import serializers
from .models import WorkingHours


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = ['id', 'doctor', 'day_of_week', 'start_time', 'end_time']
        redad_only_fields = ['id']
