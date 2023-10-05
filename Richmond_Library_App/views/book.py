from django.views import View
from django.shortcuts import render

class Book(View):
  def get(self, request):
    return render(request, "book.html", {})
  