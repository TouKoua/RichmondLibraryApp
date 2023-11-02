from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User, Book

class BookPage(View):
  def get(self, request, bookname):
    # gets specific book information via bookname
    return render(request, "book.html", {'book': get_book(bookname)})

  def post(self, request, bookname):
    book = get_book(bookname)

    if not check_availability(book):
      message = 'book is not available'
      return render(request, "book.html", {'book': book, 'message': message})
    
    book.available = book.available - 1
    book.save()

    current_user = request.user
    current_user.reserved_books.add(book)
    current_user.save()
    
    message = 'Book was reservered!'


    return render(request, "book.html", {'book': book, 'message': message})
  
def get_book(booktitle):
  return Book.objects.get(title=booktitle)

def check_availability(book):
  if book.available > 0:
    return True
  return False