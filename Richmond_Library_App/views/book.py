from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
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

class EditBook(View):
    def get(self, request, book_id):
        if get_user_status(request) != 'admin':
          return redirect('/home/')
      
      
        book = get_object_or_404(Book, id=book_id)
        return render(request, "editBook.html", {'book': book})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        # Update book attributes based on the POST data
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.genre = request.POST.get('genre')
        book.isbn = request.POST.get('isbn')
        book.year = request.POST.get('year')
        book.publisher = request.POST.get('publisher')
        book.copies = request.POST.get('copies')
        book.available = request.POST.get('available')

        # Handle image upload separately if needed
        if 'image' in request.FILES:
            book.image = request.FILES['image']

        book.save()

        # Redirect to the books page or any other page you prefer
        return redirect('Home')
