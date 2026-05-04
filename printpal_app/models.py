from django.db import models
from django.contrib.auth.models import AbstractUser


class PrintUser(AbstractUser):
    codename = models.CharField(max_length=150, unique=True, default="temp")
    email = models.EmailField(unique=True)


class Printer(models.Model):
    class PrinterStatus(models.TextChoices):
        IN_WORK = "in work"
        REPAIR = "repair"
        OUT_OF_ORDER = "out of order"

    name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=PrinterStatus.choices,
        default=PrinterStatus.IN_WORK
    )


class Material(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return f"{self.name}"


class Filament(models.Model):
    # class FilamentStatus(models.TextChoices):
    #     FULL = "full", "Full"
    #     PARTIAL = "partial", "Partial"
    #     LOW = "low", "Low"
    #     EMPTY = "empty", "Empty"
    class WeightOpts(models.TextChoices):
        LIGHT = "0.75"
        REGULAR = "0.85"
        HEAVY = "3.0"

    brand = models.CharField(max_length=100)
    weight = models.CharField(
        choices=WeightOpts.choices,
        default=WeightOpts.REGULAR)
    color = models.CharField(max_length=50, unique=True)
    material = models.ManyToManyField(Material)
    amount = models.IntegerField(default=0)
    # status = models.CharField(
    #     max_length=10,
    #     choices=FilamentStatus.choices,
    #     default=FilamentStatus.FULL
    # )

    def __str__(self):
        return f"{self.brand} {self.color} ({self.material})"


class PrintJob(models.Model):
    model_name = models.CharField(max_length=255)
    time = models.IntegerField(default=0)  # Time in hours
    filament = models.ManyToManyField(Filament)


class MyPrintPal(models.Model):
    user = models.OneToOneField(PrintUser, on_delete=models.CASCADE)
    pal_name = models.CharField(max_length=255)
    pal_animal = models.CharField(
        choices=[
            ("dog", "Dog"),
            ("cat", "Cat"),
            ("racoon", "Racoon"),
            ("rabbit", "Rabbit"),],
        default="racoon"
    )
