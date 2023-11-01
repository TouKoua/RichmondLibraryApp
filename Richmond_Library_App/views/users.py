from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User

class UsersPage(View):
    def get(self, request):
        # Gets list of all users and passes it to the user page
        users = User.objects.all()
        return render(request, "users.html", {'users': users})
    
class EditUser(View):
    def get(self, request, user):
        # Passes the user received from pressing edit button to the edit page
        return render(request, "edituser.html", {'user': user})
    
    def post(self, request, user):
        user.username = request.POST.get("_username")
        return render(request, "users.html")
    
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
