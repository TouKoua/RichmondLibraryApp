from django.test import TestCase, Client
from Richmond_Library_App.models import Book
from Richmond_Library_App.views.result import filterbooks

class ElasticSearchTests(TestCase):
    def setup(self):
        self.client = Client()
        Book.objects.create(title="The Way of Kings", author="Sanderson, Brandon", isbn=9780765365279, year=2011, publisher="Tor Fantasy", copies=1, available=1).save()
        Book.objects.create(title="Word of Radiance", author="Sanderson, Brandon", isbn=9780765365286, year=2015, publisher="Tor Fantasy", copies=1, available=1)
        Book.objects.create(title="Oathbringer", author="Sanderson, Brandon", isbn=9783453270381, year=2017, publisher="Tor Fantasy", copies=1, available=1)
        Book.objects.create(title="Rhythm of War", author="Sanderson, Brandon", isbn=9780765326386, year=2020, publisher="Tor Books", copies=1, available=1)
        Book.objects.create(title="Harry Potter and the Sorcercer's Stone", author="J.K. Rowling", isbn=9780590353427, year=1997, publisher="Scholastic", copies=1, available=1).save()
        Book.objects.create(title="Harry Potter and the Chamber of Secrets", author="J.K. Rowling", isbn=9780439064866, year=1998, publisher="Scholastic", copies=1, available=1).save()
    
    def test_titleSearch(self):
        expectedResult = list(Book.objects.filter(title="harry"))
        actualResult = filterbooks("harry", "Title")
        self.assertEquals(expectedResult,actualResult, "wrong result")