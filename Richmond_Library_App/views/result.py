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
                booklist = list(BookDocument.search().query("match", title=searchquery))
        elif filter == "Author":
                booklist = list(BookDocument.search().query("match", author=searchquery))
        elif filter == 'Publisher':
                booklist = list(BookDocument.search().query("match", publisher=searchquery))
        elif filter == 'Genre':
                # booklist = list(GenreDocument.search().query("match", genre_name=searchquery))
                # genre_object = Genre.objects.get(genre_name = booklist[0].genre_name)
                booklist = list(Genre.objects.get(genre_name = searchquery).book.all())

    except Exception as error:
        return booklist
    return booklist