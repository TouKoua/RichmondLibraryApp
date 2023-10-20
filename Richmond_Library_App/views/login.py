from django.views import View
from django.shortcuts import render, redirect
from django.forms import ModelForm
from Richmond_Library_App.models import User, Book

class Login(View):
  
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        # grabs the username and password provided
        # from the form on login.html
        name = request.POST.get('username')
        password = request.POST.get('password')
        
        # This is an if statement that uses the checkUser
        # function to validify that the given username
        # has an associated user in the database.
        # for some reason it does not display message to
        # login.html, will fix later.
        if checkUser(name) == False:
            context = {'errorMessage': 'User does not exist'}
            return render(request, 'login.html', context)
        
        # function that checks if the associated username
        # and password are of administrative status
        if Admin(name, password):
            request.session['name'] = name
            request.session['password'] = password
            return redirect('/home/')
        else:
            return render(request, "login.html", {"errorMessage": "Invalid username or password"})
        

# function that checks if the given username and password
# of associated with an administrative account        
def Admin(name, password):
    user = User.objects.get(username=name, password=password)
    if user.user_type == 'admin':
        return True

# function that checks if user is within the database
def checkUser(name):
    try:
        user = User.objects.get(username=name)
    except:
        return False
    return True