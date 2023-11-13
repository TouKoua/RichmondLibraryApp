from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User, Book

class BookPage(View):
  def get(self, request, bookname):
    # gets specific book information via bookname
    return render(request, "book.html", {'book': get_book(bookname), 'status': get_user_status(request)})

  def post(self, request, bookname):
    book = get_book(bookname)
    current_user = request.user
    user_books = current_user.reserved_books.all()

    if not check_availability(book):
      message = 'book is not available'
      return render(request, "book.html", {'book': book, 'message': message, 'status': get_user_status(request)})
    elif reserve_check(book, user_books):
      message = 'book is already reserved'
      return render(request, "book.html", {'book': book, 'message': message, 'status': get_user_status(request)})
    
    book.status = 'reserved'
    current_user.reserved_books.add(book)
    current_user.save()
    user_books = current_user.reserved_books.all()

    if not reserve_check(book, user_books):
      message = 'book was unable to be reserved'
      return render(request, "book.html", {'book': book, 'message': message, 'status': get_user_status(request)})

    book.available = book.available - 1
    book.save()
    message='book was added!'

    return render(request, "book.html", {'book': book, 'message': message, 'status': get_user_status(request)})
  
def get_book(booktitle):
  return Book.objects.get(title=booktitle)

def check_availability(book):
  if book.available > 0:
    return True
  return False

def reserve_check(book, userbooks):
    if book in userbooks:
      return True
    return False
  
def get_user_status(request):
    user = User.objects.get(username=request.user.username)
    return user.user_type