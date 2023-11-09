import django.db.models as models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Moved Books model to work with User's ManyToMany fields.
class Book(models.Model):
    """
        Model to represent Books of the library application
        containing the title, author, isbn, year, publisher,
        number of copies, and number available.
    """
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=14)
    year = models.IntegerField()
    publisher = models.CharField(max_length=100)
    copies = models.IntegerField()
    available = models.IntegerField()
    image = models.ImageField(upload_to='static\images', null=True, blank=True)

    reserved = models.BooleanField(default=False)
    checkedout = models.BooleanField(default=False)

    # added available
    def __str__(self):
        return self.title
        

# Note, we are not using this for login. We will eventually have to decide if we want to stick with this model or update it to use Django's base user model.
class User(AbstractUser):
    """
        Model to represent Users of the library application
        containing the username, password, name, email, and
        usertype.
    """
    # could probably remove username as a field and have email be
    # a unique identifier instead.
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    # removing the name field because django base model already has first_name and last_name as fields.
    email = models.EmailField(max_length=254)
    user_type = models.CharField(max_length=10) # added user type

    reserved_books = models.ManyToManyField(Book, null=True, blank=True)
    
    def __str__(self):
        return self.username


class Genre(models.Model):
    genre_name = models.CharField(max_length=100, unique=True)
    book = models.ManyToManyField(Book, null=True)
    
    def __str__(self):
        return self.genre_name

class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.collection_name