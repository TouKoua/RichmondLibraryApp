from django.views import View
from django.shortcuts import render
from django.forms import ModelForm




class Test(View):
  
    def get(self, request):
        return render(request, "login.html", {})
    