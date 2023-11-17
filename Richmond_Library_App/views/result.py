from django.views import View
from django import forms
from django.shortcuts import render
from Richmond_Library_App.document import BookDocument, GenreDocument
from Richmond_Library_App.models import Genre, Book, User

class FilterForm(forms.Form):
    author = forms.CharField(initial="", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    publisher = forms.CharField(initial="", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    available = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)

class Result(View):
    def get(self, request):
        searchquery = request.GET.get('searchquery')
        filter = request.GET.get('filter')
        result = filterbooks(searchquery, filter)
        filterForm = FilterForm(use_required_attribute=False)
        if not result:
            return render(request, 'result.html', {'message': 'No books exist given the prompt.', 
            "filterForm": filterForm,
            'status': get_user_status(request)})
        return render(request, "result.html", {"result": result, 
        "filterForm": filterForm,
        'status': get_user_status(request)})
    
    def post(self, request):
        filterForm = FilterForm(use_required_attribute=False, data=request.POST)
        searchquery = request.GET.get('searchquery')
        filter = request.GET.get('filter')
        result = filterbooks(searchquery, filter)
        if filterForm.is_valid():
            authorFilter = filterForm.cleaned_data["author"]
            publisherFilter = filterForm.cleaned_data["publisher"]
            availableFilter = filterForm.cleaned_data["available"]
            print(publisherFilter)
            for book in result:
                removed = False
                if(authorFilter):
                    if(book.author != authorFilter and not removed):
                        result.remove(book)
                        removed = True
                if(publisherFilter):
                    if(book.publisher != publisherFilter and not removed):
                        result.remove(book)
                        removed = True
                if(availableFilter):
                    if(book.available < 1 and not removed):
                        result.remove(book)
                        removed = True
        if not result:
            return render(request, 'result.html', {'message': 'No books exist given the prompt.',
             "filterForm": filterForm,
             'status': get_user_status(request),})
        return render(request, "result.html", {"result": result, 
        "filterForm": filterForm,
        'status': get_user_status(request)})
    
def filterbooks(searchquery, filter):
    try:
        if filter == "Title":
                qs = BookDocument.search().query("match", title=searchquery)
                qs = qs.to_queryset()
                booklist = list(qs)
        elif filter == "Author":
                qs = BookDocument.search().query("match", author=searchquery)
                qs = qs.to_queryset()
                booklist = list(qs)
        elif filter == 'Publisher':
                qs = BookDocument.search().query("match", publisher=searchquery)
                qs = qs.to_queryset()
                booklist = list(qs)
        elif filter == 'Genre':
                # Query for the specfic genre
                qs = GenreDocument.search().filter("match", genre_name=searchquery)
                # Change it to django queryset
                qs = qs.to_queryset()
                # Get the book list from the many to many field
                booklist = list(qs[0].book.all())

    except Exception as error:
        return booklist

    return booklist

def get_user_status(request):
    user = User.objects.get(username=request.user.username)
    return user.user_type