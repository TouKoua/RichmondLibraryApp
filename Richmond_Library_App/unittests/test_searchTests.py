from django.test import TestCase, Client
from Richmond_Library_App.models import Book, Genre
from Richmond_Library_App.views.result import filterbooks
from collections import Counter

class ElasticSearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        Book.objects.create(title="The Way of Kings", author="Sanderson, Brandon", isbn=9780765365279, year=2011, publisher="Tor Fantasy", image="book1", copies=1, available=1, status="")
        Book.objects.create(title="Word of Radiance", author="Sanderson, Brandon", isbn=9780765365286, year=2015, publisher="Tor Fantasy", image="book2", copies=1, available=1, status="")
        Book.objects.create(title="Oathbringer", author="Sanderson, Brandon", isbn=9783453270381, year=2017, publisher="Tor Fantasy", image="book3", copies=1, available=1, status="")
        Book.objects.create(title="Rhythm of War", author="Sanderson, Brandon", isbn=9780765326386, year=2020, publisher="Tor Books", image="book4", copies=1, available=1, status="")
        Book.objects.create(title="Harry Potter and the Sorcercer's Stone", author="J.K. Rowling", isbn=9780590353427, year=1997, publisher="Scholastic", image="book5", copies=1, available=1, status="")
        Book.objects.create(title="Harry Potter and the Chamber of Secrets", author="J.K. Rowling", isbn=9780439064866, year=1998, publisher="Scholastic", image="book6", copies=1, available=1, status="")
        
    def test_TitleSearch(self):
        expected = list(Book.objects.filter(title__contains = "harry"))
        actual = filterbooks("harry", "Title")
        self.assertTrue(Counter(expected) == Counter(actual))
    
    def test_TitleSearchNoMatch(self):
        expected = []
        actual = filterbooks("book1", "Title")
        self.assertListEqual(expected, actual, "Not Matching")
    
    def test_AuthorSearch(self):
        expected = list(Book.objects.filter(author__contains = "brandon"))
        actual = filterbooks("brandon", "Author")
        self.assertTrue(Counter(expected) == Counter(actual))
    
    def test_AuthorSearchNoMatch(self):
        expected = []
        actual = filterbooks("author1", "Author")
        self.assertListEqual(expected, actual, "Not Matching")
    
    def test_PublisherSearch(self):
        expected = list(Book.objects.filter(publisher__contains = "tor"))
        actual = filterbooks("tor", "Publisher")
        self.assertTrue(Counter(expected) == Counter(actual))
    
    def test_PublisherSearchNoMatch(self):
        expected = []
        actual = filterbooks("somepublisher", "Publisher")
        self.assertListEqual(expected, actual, "Not Matching")
    
    
    