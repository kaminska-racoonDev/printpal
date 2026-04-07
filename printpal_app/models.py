from django.db import models
from django.contrib.auth.models import AbstractUser


class PrintUser(AbstractUser):
    pass


class Printer(models.Model):
    name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class Filament(models.Model):
    class SpoolStatus(models.TextChoices):
        FULL = "full", "Full"
        PARTIAL = "partial", "Partial"
        LOW = "low", "Low"
        EMPTY = "empty", "Empty"

    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    status = models.CharField(
        max_length=10,
        choices=SpoolStatus.choices,
        default=SpoolStatus.FULL
    )

    def __str__(self):
        return f"{self.brand} {self.color} ({self.material}) — {self.status}"


class PrintJob(models.Model):
    model_name = models.CharField(max_length=255)
    time = models.IntegerField(default=0)  # Time in hours
    filament = models.ManyToManyField(Filament)