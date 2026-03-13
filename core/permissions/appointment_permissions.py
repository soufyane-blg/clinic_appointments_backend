from rest_framework.permissions import BasePermission


class IsDoctorOwnerOfAppointment(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user