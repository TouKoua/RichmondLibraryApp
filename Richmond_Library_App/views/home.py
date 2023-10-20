from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import User, Book  # Import the Book model

def has_permission1(user):
    return user.has_perm('auth.view')
    # Replace 'auth.view_user' with the actual permission string for permission1

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

# Convert the class-based view to a function-based view using .as_view()
home_view = Home.as_view()

# Apply the @user_passes_test decorator to the function-based view
home_view_with_permission = user_passes_test(has_permission1)(home_view)