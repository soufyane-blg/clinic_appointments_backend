from django.db import models


class Organization(models.Model):

    name = models.CharField(max_length=255)

    address = models.TextField()

    phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
