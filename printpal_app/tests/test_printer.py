from django.test import TestCase
from django.urls import reverse
from printpal_app.models import Printer
from .helpers import AuthRequiredMixin, make_user, make_printer


class PrinterCreateTest(AuthRequiredMixin, TestCase):
    def setUp(self):
        self.user = make_user()
        self.client.login(username="testuser", password="Str0ng!Pass")
        self.url = reverse("printpal_app:printer-create")

    def test_create_printer(self):
        response = self.client.post(
            self.url,
            {
                "name": "Ender 3 Pro",
                "model_name": "Ender 3 Pro",
                "status": Printer.PrinterStatus.IN_WORK,
            },
        )
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(
            Printer.objects.filter(name="Ender 3 Pro", user=self.user).exists()
        )

    def test_printer_list_visible(self):
        make_printer(self.user)
        response = self.client.get(reverse("printpal_app:printer-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Printer One")
