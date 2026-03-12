from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import WorkingHours
from .serializers import WorkingHoursSerializer

class WorkingHoursViewSet(viewsets.ModelViewSet):
    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer
    permission_classes = [IsAuthenticated]
