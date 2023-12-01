from django.test import TestCase, Client
from Richmond_Library_App.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class LoginTests(TestCase):
    def setUp(self):
        self.client = Client()
        password = 'password123'
        self.password = make_password(password)
        User.objects.create(username="test", password=self.password, email="test@email.com", user_type="student")
    
    def test_user_login(self):
        self.user = authenticate(username='test', password='password123') 
        login = self.client.login(username='test', password='password123') 
        self.assertTrue(login)
        