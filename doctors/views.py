from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import DoctorProfile
from .serializers import DoctorProfileSerializer

from core.permissions import IsAdminOrStaff


class DoctorProfileViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaff]

    def get_queryset(self):
        return DoctorProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save()