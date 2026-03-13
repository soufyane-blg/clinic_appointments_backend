from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import WorkingHours
from .serializers import WorkingHoursSerializer

from core.permissions import IsAdminOrStaff, IsDoctor


class WorkingHoursViewSet(viewsets.ModelViewSet):
    serializer_class = WorkingHoursSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrStaff | IsDoctor
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return WorkingHours.objects.all()

        return WorkingHours.objects.filter(doctor=user)

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            serializer.save()
        else:
            serializer.save(doctor=user)