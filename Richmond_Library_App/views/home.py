from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from Richmond_Library_App.models import User, Book  # Import the Book model

@method_decorator(login_required, name="get")
class Home(View):
    def get(self, request):

        # Retrieve a limited list of books from the database (limiting to num_books_to_display)
        books = Book.objects.all()

        # Pass the list of books to the template context
        context = {'books': books}

        # Render the template with the context data
        return render(request, "home.html", context)
