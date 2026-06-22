from django.test import TestCase
from django.urls import reverse
from printpal_app.models import Brand
from .helpers import AuthRequiredMixin, make_user, make_brand


class BrandCreateTest(AuthRequiredMixin, TestCase):
    def setUp(self):
        self.user = make_user()
        self.client.login(username="testuser", password="Str0ng!Pass")
        self.url = reverse("printpal_app:brand-create")

    def test_create_brand(self):
        response = self.client.post(
            self.url,
            {"name": "Monofilament", "note": "Good brand"},
        )
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(Brand.objects.filter(
            name="Monofilament", user=self.user).exists())

    def test_brand_list_visible(self):
        make_brand(self.user, "Monofilament")
        response = self.client.get(reverse("printpal_app:brands-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Monofilament")
