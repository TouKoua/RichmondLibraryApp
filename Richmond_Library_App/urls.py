"""
URL configuration for Richmond_Library_App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Richmond_Library_App.views.home import Home
from Richmond_Library_App.views.login import Login, Logout
from Richmond_Library_App.views.result import Result
from Richmond_Library_App.views.book import BookPage
from Richmond_Library_App.views.users import UsersPage, EditUser
from Richmond_Library_App.views.profile import Profile 
from Richmond_Library_App.views.addBook import BookCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name = "Login"),
    path("accounts/", include("allauth.urls")),
    path('logout/', Logout.as_view(), name="Logout"),
    path('home/', Home.as_view(), name="Home"),
    # <str:bookname> will set url to be modifiable depending on
    # the book name.
    path('book/<str:bookname>/', BookPage.as_view(), name="Book"),
    path('users/', UsersPage.as_view(), name="Users"),
    path('users/edituser', EditUser.as_view(), name="CreateUser"),
    path('add_book/', BookCreateView.as_view(), name='AddBook'),
    path('result/', Result.as_view(), name="Result"),
    path('profile/', Profile.as_view(), name="Profile"),
]
