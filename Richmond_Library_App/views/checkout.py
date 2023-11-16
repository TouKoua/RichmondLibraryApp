from django.shortcuts import render, redirect
from django.views import View
from Richmond_Library_App.models import User, Book

class Checkout(View):
    def get(self,request):
        if get_user_status(request) != 'admin' and get_user_status(request) != 'teacher':
            return redirect('/home/')
        
        context = {'users': get_users(), 'status': get_user_status(request)}
        return render(request, 'checkout.html', context)
    
    def post(self, request):
        context = {}
        
        if 'select_user' in request.POST:
            user_request = request.POST.get('userselect')
            user_request = User.objects.get(email=user_request)
            reserved_books = user_request.reserved_books.all()
            context = {'users': get_users(), 'user_books': reserved_books, 'user_email': user_request.email, 'status': get_user_status(request)}
            
        elif 'save' in request.POST:
            book_request = request.POST.get('book-status')
            user_request = request.POST.get('save')
            reserved_books = User.objects.get(email=user_request).reserved_books.all()
            
            book_option = book_request[len(book_request)-1: len(book_request)]
            book_request = Book.objects.get(title=book_request[0: len(book_request)-1])
            
            if book_option == '1':
                book_request.status = 'reserved'
                book_request.save()
            elif book_option == '2':
                book_request.status = 'checked out'
                book_request.save()
            context = {'users': get_users(), 'user_books': reserved_books, 'user_email': user_request, 'status': get_user_status(request)}
            
        
        return render(request, 'checkout.html', context)


def get_users():
    return User.objects.all()

def get_user_status(request):
    user = User.objects.get(username=request.user.username)
    return user.user_type