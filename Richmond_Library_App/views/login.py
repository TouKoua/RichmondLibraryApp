from django.views import View
from django.shortcuts import render, redirect
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
        print("HERE: ", name, password)

        user = authenticate(request, username=name, password=password)
        print("User: ", user)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, "login.html", {"errorMessage": "Invalid username or password"})

class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, "login.html", {"errorMessage": "You have been logged out!"})
    
    # This is for relogging into the app after clicking the logout button
    def post(self, request):
        # grabs the username and password provided
        # from the form on login.html
        name = request.POST.get('username')
        password = request.POST.get('password')
        # This is now using Django's Authentification system.
        request.session['name'] = name
        request.session['password'] = password
        print("HERE: ", name, password)

        user = authenticate(request, username=name, password=password)
        print("User: ", user)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, "login.html", {"errorMessage": "Invalid username or password"})