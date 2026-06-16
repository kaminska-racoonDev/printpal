from django.test import Client
from printpal_app.models import PrintUser, Brand, Filament, Printer


def make_user(username="testuser", password="Str0ng!Pass", email="test@test.com"):
    return PrintUser.objects.create_user(
        username=username,
        email=email,
        password=password,
    )


def make_brand(user, name="BrandX"):
    return Brand.objects.create(user=user, name=name, note="test note")


def make_filament(user, brand):
    return Filament.objects.create(
        user=user,
        brand=brand,
        weight=Filament.WeightOpts.REGULAR,
        color="Red",
        color_code="#ff0000",
        material=Filament.MaterialOpts.PLA,
        amount=2,
        priority=1,
    )


def make_printer(user, name="Printer One"):
    return Printer.objects.create(
        user=user,
        name=name,
        model_name="Ender 3",
        status=Printer.PrinterStatus.IN_WORK,
    )


class AuthRequiredMixin:
    def test_redirects_when_not_logged_in(self):
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/", response["Location"])
