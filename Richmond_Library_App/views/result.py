from django.views import View
from django.shortcuts import render
from Richmond_Library_App.document import BookDocument




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
    except Exception as error:
        return booklist
    return booklist