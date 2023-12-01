import sys
sys.path.append(r"C:\Users\Proje\Desktop\Projects\RichmondLibraryApp")
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Richmond_Library_App.settings")
django.setup()

from django.test import TestCase, Client
from django.urls import reverse
from Richmond_Library_App.models import User

class LoginTestCase(TestCase): 
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('Login')  # Using correct name 'Login'
        self.home_url = reverse('Home')  # Using correct name 'Home'
        # Create a test user for login
        self.user = User.objects.create(username='testuser', password='password123', email='testuser@example.com')

    def test_login_user(self):
        # Attempt to log in with valid credentials
        login_data = {'username': 'testuser', 'password': 'password123', 'email' : 'testuser@example.com'}
        response = self.client.post(self.login_url, login_data, follow=True)
        
        # Check if the user is redirected to the home page upon successful login
        self.assertRedirects(response, self.home_url)
        # Check if the user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)
