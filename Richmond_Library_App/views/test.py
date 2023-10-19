from django.views import View
from django.shortcuts import render
from Richmond_Library_App.document import BookDocument




class Test(View):
  
    def get(self, request):
        searchquery = request.GET.get('searchquery')
        result = BookDocument.search().query("match", title=searchquery)
        qs = result.to_queryset()
        return render(request, "test.html", {"result":qs})