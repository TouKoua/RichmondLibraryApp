from django.contrib import admin
from Richmond_Library_App.models import User, Book, Genre, Collection

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Collection)
