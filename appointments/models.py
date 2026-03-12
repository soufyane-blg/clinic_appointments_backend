from django.db import models

class Appointment(models.Model):

    STATUS_CHOICES = [
        ("SCHEDULED", "Scheduled"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
        ("NO_SHOW", "No Show"),
    ]

    doctor = models.ForeignKey(
        "doctors.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    patient = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="patient_appointments"
    )

    date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="SCHEDULED"
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "start_time"]


class AppointmentNote(models.Model):

    appointment = models.OneToOneField(
        "appointments.Appointment",
        on_delete=models.CASCADE,
        related_name="note"
    )

    doctor = models.ForeignKey(
        "doctors.DoctorProfile",
        on_delete=models.CASCADE
    )

    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
