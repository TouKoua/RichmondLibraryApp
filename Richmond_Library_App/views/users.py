from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User

class UsersPage(View):
    def get(self, request):
        # gets specific user information via bookname
        users = User.objects.all()
        return render(request, "users.html", {'users': users})
    
class EditUser(View):
    def get(self, request):
        return render(request, "edituser.html")
    
    # def post(self, request):
    #     User.objects.create(
    #         username=request.POST.get("username"),
    #         password=request.POST.get("password"),
    #         name=request.POST.get("name"),
    #         email=request.POST.get("email"),
    #         user_type=request.POST.get("user_type")
    #     )
    #     users = User.objects.all()
    #     return render(request, "users.html", {'users': users})
