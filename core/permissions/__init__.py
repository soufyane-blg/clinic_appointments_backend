from .role_permissions import (
    IsAdmin,
    IsStaff,
    IsAdminOrStaff,
    IsDoctor,
)

from .appointment_permissions import (
    IsDoctorOwnerOfAppointment,
)



from .schedule_permissions import (
    IsDoctorOwnerOfSchedule,
)

__all__ = [
    "IsAdmin",
    "IsStaff",
    "IsAdminOrStaff",
    "IsDoctor",
    "IsDoctorOwnerOfAppointment",
    "IsDoctorOwnerOfSchedule",
]