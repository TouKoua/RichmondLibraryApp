from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User, Book

class BookPage(View):
  def get(self, request, bookname):
    # gets specific book information via bookname
    book = Book.objects.get(title=bookname)
    return render(request, "book.html", {'book': book})
  