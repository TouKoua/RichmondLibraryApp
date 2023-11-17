from django.views import View
from django.shortcuts import render, redirect
from django import forms
from django.core.paginator import Paginator
from Richmond_Library_App.models import User, Book, Collection

class AddBookToCollectionForm(forms.ModelForm):
    collection_name = forms.CharField(max_length=100)  # Add a field for the collection name

    class Meta:
        model = Collection
        fields = ['book', 'collection_name']  # Include the new field

class Profile(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("http://127.0.0.1:8000/")
        
        user = User.objects.get(username=request.user.username)
        book_list = user.reserved_books.all()
        
        # Create an instance of the form for adding a book to the collection
        add_book_form = AddBookToCollectionForm()
        
        # Fetch the user's book collection
        user_collection = Collection.objects.filter(user=user)

        # Pagination for collections
        collections_per_page = 10  # Adjust the number of collections per page
        collections_paginator = Paginator(user_collection, collections_per_page)
        collections_page_number = request.GET.get('collections_page')
        collections_page = collections_paginator.get_page(collections_page_number)

        # Pagination for books
        books_per_page = 10  # Adjust the number of books per page
        books_paginator = Paginator(book_list, books_per_page)
        books_page_number = request.GET.get('books_page')
        books_page = books_paginator.get_page(books_page_number)
        
        return render(request, "profile.html", {
            "user": user,
            "add_book_form": add_book_form,
            "user_collection": collections_page,
            "books": books_page,
            'status': get_user_status(request),
        })

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('')
        
        user = User.objects.get(username=request.user.username)
        user_collection = Collection.objects.filter(user=user)
        
        # Create Collection Modal Form
        if 'create_collection' in request.POST:
            # Handle the Create Collection action
            add_book_form = AddBookToCollectionForm(data=request.POST)
            if add_book_form.is_valid():
                collection_entry = add_book_form.save(commit=False)
                collection_entry.user = request.user
                collection_entry.save()
                add_book_form.save_m2m()
                return render(request, "profile.html", {"user": user, 
                "add_book_form": add_book_form, 
                "user_collection": user_collection, 
                "message": "Created new collection!",
                'status': get_user_status(request)})
            else:
                return render(request, "profile.html", {"user": user, 
                "add_book_form": add_book_form, 
                "user_collection": user_collection, 
                "message": "Unable to create collection",
                'status': get_user_status(request)})

        elif 'view_collections' in request.POST:
            # Handle the View Collections action
            # You can redirect the user to a page to view their collections

            # Fetch the user's book collection
            user_collection = Collection.objects.filter(user=user)

        return render(request, "profile.html", {"user": user, 
        "add_book_form": add_book_form, 
        "user_collection": user_collection,
        'status': get_user_status(request),})

def get_user_status(request):
    user = User.objects.get(username=request.user.username)
    return user.user_type
