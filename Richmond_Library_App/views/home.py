from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import User, Book  # Import the Book model

class Home(View):
    def get(self, request):
        # Set the number of books you want to display on the homepage
        num_books_to_display = 9  # Can change this to the desired number

        # Retrieve a limited list of books from the database (limiting to num_books_to_display)
        books = Book.objects.all()[:num_books_to_display]

        # Pass the list of books to the template context
        context = {'books': books}

        # Render the template with the context data
        return render(request, "home.html", context)
