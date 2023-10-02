from django.views import View
from django.shortcuts import render, redirect
from django.forms import ModelForm
from Richmond_Library_App.models import User



class Login(View):
  
    def get(self, request):
        return render(request, "login.html", {})
    
    def post(self, request):
        name = request.POST.get('username')
        password = request.POST.get('password')
        if User().login(name, password):
            request.session['name'] = name
            request.session['password'] = password
            return redirect('/home/')

        else:
            return render(request, "login.html", {"errorMessage": "Invalid username or password"})  



    
    # def post(self, request):
    #     name = request.POST.get('name')
    #     password = request.POST.get('password')
    #     if Admin().login(name, password):
    #         request.session['name'] = name
    #         request.session['password'] = password
    #         return redirect('/home/')

    #     else:
    #         return render(request, "login.html", {"errorMessage": "Invalid username or password"})