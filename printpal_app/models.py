from django.db import models
from django.contrib.auth.models import AbstractUser


class PrintUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)


class Printer(models.Model):
    user = models.ForeignKey(PrintUser, on_delete=models.CASCADE)

    class PrinterStatus(models.TextChoices):
        IN_WORK = "In work"
        REPAIR = "Repair"
        OUT_OF_ORDER = "Out of order"

    name = models.CharField(max_length=255, unique=True)
    model_name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=PrinterStatus.choices,
        default=PrinterStatus.IN_WORK
    )


class Brand(models.Model):
    user = models.ForeignKey(PrintUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Filament(models.Model):
    user = models.ForeignKey(PrintUser, on_delete=models.CASCADE)

    class WeightOpts(models.TextChoices):
        LIGHT = "0.75", "0.75 kg"
        REGULAR = "0.85", "0.85 kg"
        HEAVY = "3.0",  "3.0 kg"

    class MaterialOpts(models.TextChoices):
        PLA = "PLA", "pla"
        PETG = "PETG", "petg"
        ABS = "ABS", "abs"
        TPU = "TPU", "tpu"

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='filaments'
    )
    weight = models.CharField(
        choices=WeightOpts.choices,
        default=WeightOpts.REGULAR)
    color = models.CharField(max_length=50)
    color_code = models.CharField(max_length=7, default="#ffffff")
    material = models.CharField(
        max_length=15,
        choices=MaterialOpts.choices,
        default=MaterialOpts.PLA
    )
    amount = models.IntegerField(default=0)
    priority = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return f"{self.brand} {self.color} ({self.material})"


class PrintJob(models.Model):
    user = models.ForeignKey(PrintUser, on_delete=models.CASCADE)

    model_name = models.CharField(max_length=255)
    time = models.FloatField(default=0)
    filament = models.ManyToManyField(Filament)
    image = models.URLField(blank=True)
    note = models.TextField(blank=True)


class MyPrintPal(models.Model):
    user = models.ForeignKey(PrintUser, on_delete=models.CASCADE)

    pal_name = models.CharField(max_length=255)
    pal_animal = models.CharField(
        choices=[
            ("patchy dog", "Patchy Dog"),
            ("white dog", "White Dog"),
            ("cat", "Cat"),
            ("racoon", "Racoon"),],
        default="racoon"
    )
