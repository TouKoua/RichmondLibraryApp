from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import User, Book
from django.shortcuts import redirect



class BookCreateView(View):
    def get(self,request):
        return render(request, 'addBook.html', {})
    
    def post(self, request):
        title = request.POST.get("title")
        author = request.POST.get("author")
        isbn = request.POST.get("isbn")
        year = request.POST.get("year")
        publisher = request.POST.get("publisher")
        image = request.FILES['image']
        copies = request.POST.get("copies")
        available = request.POST.get("available")
        message = ""
        if(not isinstance(title,str) or
           (not isinstance(author,str)) or
           (not isbn.isdigit()) or
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
            message = "Successfully added Book!"
            return render(request, 'addBook.html', {'message': message})

