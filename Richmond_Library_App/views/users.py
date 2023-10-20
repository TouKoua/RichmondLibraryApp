from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User

class UsersPage(View):
    def get(self, request):
        # gets specific user information via bookname
        users = User.objects.all()
        return render(request, "users.html", {'users': users})
    
class CreateUser(View):
    def get(self, request):
        return render(request, "createuser.html")
    
    def post(self, request):
        User.objects.create(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            name=request.POST.get("username"),
            email=request.POST.get("password"),
            user_type=request.POST.get("user_type")
        )
        users = User.objects.all()
        return render(request, "users.html", {'users': users})
