from django.test import TestCase
from django.urls import reverse
from printpal_app.models import PrintJob
from .helpers import AuthRequiredMixin, make_user, make_brand, make_filament


class PrintJobCreateTest(AuthRequiredMixin, TestCase):
    def setUp(self):
        self.user = make_user()
        self.client.login(username="testuser", password="Str0ng!Pass")
        self.brand = make_brand(self.user)
        self.filament = make_filament(self.user, self.brand)
        self.url = reverse("printpal_app:printjob-create")

    def test_create_printjob(self):
        response = self.client.post(
            self.url,
            {
                "model_name": "Benchy",
                "time": 2.5,
                "filament": [self.filament.pk],
                "image": "https://makerworld.bblmw.com/makerworld/model/US3f9fe757a16d44/design/2023-09-20_cfa497eb38848.jpg?x-oss-process=image/resize,w_1000/format,webp",
                "note": "Test print",
            },
        )
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(
            PrintJob.objects.filter(
                model_name="Benchy", user=self.user).exists()
        )

    def test_printjob_list_visible(self):
        job = PrintJob.objects.create(
            user=self.user,
            model_name="Benchy",
            time=2.5,
        )
        job.filament.set([self.filament])
        response = self.client.get(reverse("printpal_app:printjob-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Benchy")

    def test_printjob_detail(self):
        job = PrintJob.objects.create(
            user=self.user,
            model_name="Benchy",
            time=2.5,
        )
        job.filament.set([self.filament])
        response = self.client.get(
            reverse("printpal_app:printjob-detail", kwargs={"pk": job.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Benchy")
