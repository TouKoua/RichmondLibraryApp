from django.shortcuts import render
from django.views import View
from Richmond_Library_App.models import User, Book
from django.shortcuts import redirect



class BookCreateView(View):
    def get(self,request):
      
        return render(request, 'addBook.html', {})
    def post(self, request):
        form = Book(request.POST)
        if form.is_valid():
            form.save()
            return redirect('name_of_books_list_view')  # Replace 'name_of_books_list_view' with the actual view name.
        return render(request, 'book_form.html', {'form': form})

