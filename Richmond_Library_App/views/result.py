from django.views import View
from django.shortcuts import render
from Richmond_Library_App.document import BookDocument, GenreDocument
from Richmond_Library_App.models import Genre, Book
import requests
from Richmond_Library_App import settings

class Result(View):

    def get(self, request):
        searchquery = request.GET.get('searchquery')
        filter = request.GET.get('filter')
        result = filterbooks(searchquery, filter)
        if not result:
            return render(request, 'result.html', {'message': 'No books exist given the prompt.'})
        return render(request, "result.html", {"result": result})


def filterbooks(searchquery, filter):
    try:
        if filter == "Title":
            qs = BookDocument.search().filter("match", title=searchquery)
            qs = qs.to_queryset()
            booklist = list(qs)
        elif filter == "Author":
            qs = BookDocument.search().filter("match", author=searchquery)
            qs = qs.to_queryset()
            booklist = list(qs)
        elif filter == 'Publisher':
            qs = BookDocument.search().filter("match", publisher=searchquery)
            qs = qs.to_queryset()
            booklist = list(qs)
        elif filter == 'Genre':
            # Query for the specfic genre
            qs = GenreDocument.search().filter("match", genre_name=searchquery)
            # Change it to django queryset
            qs = qs.to_queryset()
            # Get the book list from the many to many field
            booklist = qs[0].book.all
            print(booklist)

        if not booklist:
            api_url = f'https://www.googleapis.com/books/v1/volumes?q={searchquery}&key={settings.GOOGLE_BOOKS_API_KEY}'
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                for item in data['items']:
                    book_info = item['volumeInfo']
                    # Create a Book instance for each item
                    book = Book(
                        title=book_info.get('title', ''),
                        author=', '.join(book_info.get('authors', [])),
                        # Add other fields as per your model.
                        # ...
                    )
                    booklist.append(book)
                    # Consider saving the book to the database if needed.
                    # book.save()

    except Exception as error:
        return booklist

    return booklist
