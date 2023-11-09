from elasticsearch import Elasticsearch
from Richmond_Library_App.models import Book
from django.shortcuts import redirect

def remove_book(request):
    if request.method == "GET":
        book_id = request.GET.get("book_id")

        # Delete the book from the Django database
        book = Book.objects.get(id=book_id)
        book.delete()

        # Delete the corresponding document from the Elasticsearch index
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])  # Replace with your Elasticsearch server details
        index_name = 'elastic'  # Replace with your Elasticsearch index name
        document_id = str(book_id)

        es.delete(index=index_name, id=document_id, ignore=[400, 404])

    return redirect('Home')  # Redirect to the home page or any other relevant page