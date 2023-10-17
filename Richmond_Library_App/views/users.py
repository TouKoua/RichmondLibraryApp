from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User

class UsersPage(View):
    def get(self, request):
        # gets specific user information via bookname
        users = User.objects.all()
        return render(request, "users.html", {'users': users})
    
    # def post(self, request):
    #     User.objects.create(
    #         request.POST.get("username"),
    #         request.POST.get("password"),
    #         request.POST.get("username"),
    #         request.POST.get("password"),
    #         request.POST.get("user_type")
    #     )
    #     return render(request, "")
    
class CreateUser(View):
    def get(self, request):
        return render(request, "createuser.html")
    
    def post(self, request):
        User.objects.create(
            request.POST.get("username"),
            request.POST.get("password"),
            request.POST.get("username"),
            request.POST.get("password"),
            request.POST.get("user_type")
        )
        users = User.objects.all()
        return render(request, "{% url 'Users' %}", {'users': users})
