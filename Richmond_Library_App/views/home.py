from django.contrib.auth.decorators import user_passes_test
from django.views import View
from django.shortcuts import render

def has_permission1(user):
    return user.has_perm('auth.view')
    # Replace 'auth.view_user' with the actual permission string for permission1

class Home(View):
    def get(self, request):
        return render(request, "home.html", {})

# Convert the class-based view to a function-based view using .as_view()
home_view = Home.as_view()

# Apply the @user_passes_test decorator to the function-based view
home_view_with_permission = user_passes_test(has_permission1)(home_view)