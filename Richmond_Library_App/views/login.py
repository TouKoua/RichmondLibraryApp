from django.views import View
from django.shortcuts import render, redirect
from django.forms import ModelForm
<<<<<<< HEAD
from Richmond_Library_App.models import User


=======
from Richmond_Library_App.models import User, Book
>>>>>>> main

class Login(View):
  
    def get(self, request):
        return render(request, "login.html", {})
    
    def post(self, request):
<<<<<<< HEAD
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
=======
        # grabs the username and password provided
        # from the form on login.html
        name = request.POST.get('username')
        password = request.POST.get('password')
        
        # function that checks if the associated username
        # and password are of administrative status
        if Admin(name, password):
            request.session['name'] = name
            request.session['password'] = password
            return redirect('/home/')
>>>>>>> main

        else:
            return render(request, "login.html", {"errorMessage": "Invalid username or password"})

# function that checks if the given username and password
# of associated with an administrative account        
def Admin(name, password):
    user = User.objects.get(username=name, password=password)
    if user.user_type == 'admin':
        return True