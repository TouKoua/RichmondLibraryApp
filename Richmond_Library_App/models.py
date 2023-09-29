#import django.db.models
from django.db import models

class Book(models.Model):
    #ISBN
    ISBN = models.CharField(max_length=12)
    #Title
    Title = models.CharField(max_length=100)
    #Author
    Author = models.CharField(max_length=50)
    #Publisher
    Publisher = models.CharField(max_length=50)
    #Publication_Date
    Publication_Date = models.CharField(max_length=10)
    #Entry_Date
    Entry_Date = models.CharField(max_length=10)
    #Reading_Level
    Reading_Level = models.CharField(max_length=20)
    #Genre
    Genre = models.CharField(max_length=20)
    #Quantity
    Quantity = models.CharField(max_length=4)