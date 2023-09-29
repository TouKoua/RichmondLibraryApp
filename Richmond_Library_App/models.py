#import django.db.models
from django.db import models

class Book(models.Model):
    #ISBN
    ISBN = models.CharField()
    #Title
    Title = models.CharField()
    #Author
    Author = models.CharField()
    #Publisher
    Publisher = models.CharField()
    #Publication_Date
    Publication_Date = models.CharField()
    #Entry_Date
    Entry_Date = models.CharField()
    #Reading_Level
    Reading_Level = models.CharField()
    #Genre
    Genre = models.CharField()
    #Quantity
    Quantity = models.CharField()