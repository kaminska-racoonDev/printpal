from django.test import TestCase
from django.urls import reverse
from printpal_app.models import PrintUser
from .helpers import make_user


class SignupTest(TestCase):
    def test_signup_creates_user(self):
        response = self.client.post(
            reverse("account_signup"),
            {
                "username": "newuser",
                "email": "newuser@test.com",
                "password1": "Str0ng!Pass",
                "password2": "Str0ng!Pass",
            },
        )
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(PrintUser.objects.filter(username="newuser").exists())

    def test_signup_mismatched_passwords_fails(self):
        self.client.post(
            reverse("account_signup"),
            {
                "username": "newuser2",
                "email": "newuser2@test.com",
                "password1": "Str0ng!Pass",
                "password2": "WrongPass!",
            },
        )
        self.assertFalse(PrintUser.objects.filter(
            username="newuser2").exists())


class LoginTest(TestCase):
    def setUp(self):
        self.user = make_user()

    def test_login_success(self):
        response = self.client.post(
            reverse("account_login"),
            {"login": "testuser", "password": "Str0ng!Pass"},
        )
        self.assertIn(response.status_code, [200, 302])
        self.assertIn("_auth_user_id", self.client.session)

    def test_login_wrong_password(self):
        self.client.post(
            reverse("account_login"),
            {"login": "testuser", "password": "WrongPass!"},
        )
        self.assertNotIn("_auth_user_id", self.client.session)


class LogoutTest(TestCase):
    def setUp(self):
        self.user = make_user()
        self.client.login(username="testuser", password="Str0ng!Pass")

    def test_logout(self):
        self.client.post(reverse("account_logout"))
        self.assertNotIn("_auth_user_id", self.client.session)
