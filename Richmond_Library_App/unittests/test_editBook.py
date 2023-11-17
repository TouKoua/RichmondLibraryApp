from django.test import TestCase, Client
from Richmond_Library_App.models import Book

class ElasticSearchTests(TestCase):
    def setUp(self):
        self.client = Client()