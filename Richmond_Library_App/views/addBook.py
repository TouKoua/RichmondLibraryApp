from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import Genre, Book
from django.shortcuts import redirect
from Richmond_Library_App import settings
from django.core.exceptions import ObjectDoesNotExist
import requests
from urllib.parse import quote


class BookCreateView(View):
    def get(self, request):
        return render(request, 'addBook.html', {})

    def post(self, request):
        isbn = request.POST.get("isbn")
        copies = request.POST.get("copies")
        available = request.POST.get("available")
        genre = request.POST.get("genre")
        cover_art = request.FILES['image']
        
        genre_list = uppercase_genre(genre.split(" "))
        
        book = fetch_book_from_api(isbn, cover_art, copies, available)
    
        if book:
            # Save the book if it's new (fetched from API)
            if not book.pk:
                book.save()
                # Here you can also add genres to the book as per your requirement
            message = "Successfully added Book!"
        else:
            message = "Book not found."

        print(genre_list)
        parse_genre(genre_list, book)
        return render(request, 'addBook.html', {'message': message})



def uppercase_genre(list):
    for i in range(len(list)):
        list[i] = list[i][0].upper() + list[i][1:]
    return list


def parse_genre(list, book):
    for i in list:
        try:
            genre_object = Genre.objects.get(genre_name=i)
            genre_object.book.add(book)
            genre_object.save()
        except:
            genre_object = Genre.objects.create(genre_name=i)
            genre_object.book.add(book)
            genre_object.save()


# def check_book(book):
#     try:
#         Book.objects.get(title=book.title)
#         return True
#     except:
#         return False
    

def fetch_book_from_api(isbn, cover_art, copies_num, available_num):
    encoded_isbn = quote(isbn)  # URL encode the title
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{encoded_isbn}&key={settings.GOOGLE_BOOKS_API_KEY}'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data['totalItems'] > 0:
                book_info = data['items'][0]['volumeInfo']
                return Book(
                    title=book_info.get('title', ''),
                    author=', '.join(book_info.get('authors', [])),
                    isbn=book_info.get('industryIdentifiers', [{'identifier': ''}])[
                        0]['identifier'],
                    year=book_info.get('publishedDate', '').split('-')[0],
                    publisher=book_info.get('publisher', ''),
                    copies=copies_num,
                    available=available_num,
                    # image=book_info.get('imageLinks', {}).get('thumbnail', '')
                    image=cover_art
                )
            else:
                print("No books found in the Google Books API.")
        else:
            print(f"Error fetching from Google Books API: {response.text}")
    except requests.RequestException as e:
        print(f"Requests error when fetching from Google Books API: {e}")
    return None