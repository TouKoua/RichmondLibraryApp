from django.views import View
from django.shortcuts import render
from django.forms import ModelForm




class Login(View):
  
    def get(self, request):
        return render(request, "login.html", {})
    
    # def post(self, request):
    #     name = request.POST.get('name')
    #     password = request.POST.get('password')
    #     if Admin().login(name, password):
    #         request.session['name'] = name
    #         request.session['password'] = password
    #         return redirect('/home/')

    #     else:
    #         return render(request, "login.html", {"errorMessage": "Invalid username or password"})