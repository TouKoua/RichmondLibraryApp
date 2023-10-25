from django.views import View
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.contrib.auth import authenticate, login, logout

class Login(View):
    
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        # grabs the username and password provided
        # from the form on login.html
        name = request.POST.get('username')
        password = request.POST.get('password')
        # This is now using Django's Authentification system.
        request.session['name'] = name
        request.session['password'] = password
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
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

class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, "login.html", {"errorMessage": "You have been logged out!"})