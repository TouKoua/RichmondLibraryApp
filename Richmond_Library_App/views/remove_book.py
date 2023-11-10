from elasticsearch import Elasticsearch
from Richmond_Library_App.models import Book
from django.shortcuts import redirect

def remove_book(request):
    if request.method == "GET":
        book_id = request.GET.get("book_id")

        # Delete the book from the Django database
        book = Book.objects.get(id=book_id)
        book.delete()

    return redirect('Home')  # Redirect to the home page or any other relevant page