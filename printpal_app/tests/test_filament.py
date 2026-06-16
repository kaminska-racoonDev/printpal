from django.test import TestCase
from django.urls import reverse
from printpal_app.models import Filament
from .helpers import AuthRequiredMixin, make_user, make_brand, make_filament


class FilamentCreateTest(AuthRequiredMixin, TestCase):
    def setUp(self):
        self.user = make_user()
        self.client.login(username="testuser", password="Str0ng!Pass")
        self.brand = make_brand(self.user)
        self.url = reverse("printpal_app:filament-create")

    def test_create_filament(self):
        response = self.client.post(
            self.url,
            {
                "brand": self.brand.pk,
                "weight": Filament.WeightOpts.REGULAR,
                "color": "Blue",
                "color_code": "#0000ff",
                "material": Filament.MaterialOpts.PETG,
                "amount": 3,
                "priority": 1,
            },
        )
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(
            Filament.objects.filter(color="Blue", user=self.user).exists()
        )

    def test_filament_list_visible(self):
        make_filament(self.user, self.brand)
        response = self.client.get(reverse("printpal_app:filament-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Red")

    def test_weight_label_shows_kg(self):
        filament = make_filament(self.user, self.brand)
        self.assertIn("kg", filament.get_weight_display())
        self.assertNotIn("REGULAR", filament.get_weight_display())
