from django.views import View
from django.shortcuts import render, redirect
from django.forms import ModelForm
from Richmond_Library_App.models import User, Book

class Profile(View):

    def get(self, request):

        # Check the users logged in 
        name =  request.session.get('name', None)
        if not name:
            return redirect('/login/')
        
        # Fetch user details
        user = User.objects.get(username=name)
        return render(request, "profile.html", {"user": user})
    
    def post(self, request):

        # Check the users logged in 
        name =  request.session.get('name', None)
        if not name:
            return redirect('/login/')
        
        # Fetch user details
        user = User.objects.get(username=name)
        
        # Update user details
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email_address = request.POST.get('email_address')
        user.phone_number = request.POST.get('phone_number')
        user.save()
        
        return render(request, "profile.html", {"user": user})