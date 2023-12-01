from Richmond_Library_App.models import User, Book, Genre
from django.test import TestCase

class TestRemoveBook(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test", password="test", user_type="student")
        self.book = Book.objects.create(title="test", author="test", isbn="test", year=2021, publisher="test", copies=1, available=1)
        self.book.save()
        self.user.save()
        
    def test_removeBook(self):
        self.user.reserved_books.add(self.book)
        self.user.save()
        self.assertEqual(self.user.reserved_books.count(), 1)
        self.user.reserved_books.remove(self.book)
        self.user.save()
        self.assertEqual(self.user.reserved_books.count(), 0)