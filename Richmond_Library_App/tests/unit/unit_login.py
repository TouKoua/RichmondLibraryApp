from django.test import TestCase
from project_app.models import Course, User
from project_app.classes.admin import Admin


class TestLogIn(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username="user", password="1234", email="user@example.com")
        self.admin1 = Admin()

    def test_validLogin(self):
        self.assertTrue(self.admin1.login(
            "user", "1234"), msg='should have returned true since username and password are correct')

    def test_invalidPassword(self):
        self.assertFalse(self.admin1.login(
            "user", "wrong"), msg='should have returned false since password is incorrect')

    def test_nonexistentUser(self):
        self.assertFalse(self.admin1.login("nonexistentuser", "password"),
                         msg='should have returned false since user does not exist')

    def test_invalidUsername(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid username type"):
            self.admin1.login(123, "password")

    def test_invalidPasswordType(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid password type"):
            self.admin1.login("user", 123)
