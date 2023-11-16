from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import Genre, Book, User
from django.shortcuts import redirect, redirect



class BookCreateView(View):
    def get(self,request):
        if get_user_status(request) != 'admin':
            return redirect('/home/')
        
        return render(request, 'addBook.html', {'status': get_user_status(request)})
    
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
            return render(request, "addBook.html", {"message": message, 'status': get_user_status(request)}) # Replace 'name_of_books_list_view' with the actual view name.
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
            return render(request, 'addBook.html', {'message': message, 'status': get_user_status(request)})

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


def get_user_status(request):
    user = User.objects.get(username=request.user.username)
    return user.user_type