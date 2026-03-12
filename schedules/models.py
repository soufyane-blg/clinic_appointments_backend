from django.db import models

class WorkingHours(models.Model):

    DAYS = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    doctor = models.ForeignKey(
        "doctors.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="working_hours"
    )

    day_of_week = models.IntegerField(choices=DAYS)

    start_time = models.TimeField()

    end_time = models.TimeField()

    class Meta:
        unique_together = ["doctor", "day_of_week"]



class WorkingHours(models.Model):

    DAYS = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    doctor = models.ForeignKey(
        "doctors.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="working_hours"
    )

    day_of_week = models.IntegerField(choices=DAYS)

    start_time = models.TimeField()

    end_time = models.TimeField()

    class Meta:
        unique_together = ["doctor", "day_of_week"]