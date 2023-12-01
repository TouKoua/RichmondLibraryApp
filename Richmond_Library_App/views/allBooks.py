from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import Book  # Import the Book model

class AllBooks(View):
    def get(self, request):

        # Retrieve a limited list of books from the database (limiting to num_books_to_display)
        books = Book.objects.all()

        # Pass the list of books to the template context
        context = {'books': books}

        # Render the template with the context data
        return render(request, "allBooks.html", context)