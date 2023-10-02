import django.db.models as models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    user_type = models.CharField(max_length=10) # added user type
    
    def __str__(self):
        return self.name
    
    def login(self, username, password):
        try:
            user = User.objects.get(username=username, password=password)
            return True
        except:
            return False    
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    publisher = models.CharField(max_length=100)
    copies = models.IntegerField()
    available = models.IntegerField()
    # added available
    def __str__(self):
        return self.title
