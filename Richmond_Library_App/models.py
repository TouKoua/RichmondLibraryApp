import django.db.models as models


# Create your models here.

class User(models.Model):
    """
        Model to represent Users of the library application
        containing the username, password, name, email, and
        usertype.
    """
    # could probably remove username as a field and have email be
    # a unique identifier instead.
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    user_type = models.CharField(max_length=10) # added user type
    
    def __str__(self):
        return self.name
    


class Book(models.Model):
    """
        Model to represent Books of the library application
        containing the title, author, isbn, year, publisher,
        number of copies, and number available.
    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField(default=0)
    year = models.IntegerField()
    publisher = models.CharField(max_length=100)
    copies = models.IntegerField()
    available = models.IntegerField()
    # added available
    def __str__(self):
        return self.title

class BooksToUsers(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
