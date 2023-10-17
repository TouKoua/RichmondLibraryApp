from django.views import View
from django.shortcuts import render
from Richmond_Library_App.models import User

class UsersPage(View):
    def get(self, request):
        # gets specific user information via bookname
        users = User.objects.all()
        return render(request, "users.html", {'users': users})
