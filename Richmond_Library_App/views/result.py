from django.views import View
from django.shortcuts import render
from Richmond_Library_App.document import BookDocument, GenreDocument
from Richmond_Library_App.models import Genre, Book




class Result(View):
  
    def get(self, request):
        searchquery = request.GET.get('searchquery')
        filter = request.GET.get('filter')
        result = filterbooks(searchquery, filter)
        if not result:
            return render(request, 'result.html', {'message': 'No books exist given the prompt.'})
        return render(request, "result.html", {"result":result})
    
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

    except Exception as error:
        return booklist
    return booklist