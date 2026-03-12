from django.db import models


class DoctorProfile(models.Model):

    SESSION_CHOICES = [
        (15, "15 minutes"),
        (30, "30 minutes"),
        (60, "60 minutes"),
    ]

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    specialization = models.CharField(max_length=255)

    session_duration = models.IntegerField(
        choices=SESSION_CHOICES,
        default=30
    )

    is_active = models.BooleanField(default=True)

    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Dr {self.user.first_name}"
