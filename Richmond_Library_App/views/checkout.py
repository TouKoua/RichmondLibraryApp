from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import Genre, Book



class Checkout(View):
    def get(self,request):
        return render(request, 'addBook.html', {})
    
    def post(self, request):
        title = request.POST.get("title")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        isbn = request.POST.get("isbn")
        year = request.POST.get("year")
        publisher = request.POST.get("publisher")
        image = request.FILES['image']
        copies = request.POST.get("copies")
        available = request.POST.get("available")
        message = ""
        if(not isinstance(title,str) or
           (not isinstance(author,str)) or
           (not isinstance(isbn, str)) or
           (not year.isdigit()) or
           (not isinstance(publisher,str)) or
           (not copies.isdigit()) or
           (not available.isdigit()) ):
            message = "Invalid input"
            return render(request, "addBook.html", {"message": message}) # Replace 'name_of_books_list_view' with the actual view name.
        else:
            book = Book.objects.create(title=title,
                                       author=author,
                                       isbn=isbn,
                                       year=year,
                                       publisher=publisher,
                                       image=image,
                                       copies=copies,
                                       available=available)
            book.save()
            
            genre_list = uppercase_genre(genre.split(" "))
            parse_genre(genre_list, book)
            
            
            message = "Successfully added Book!"
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