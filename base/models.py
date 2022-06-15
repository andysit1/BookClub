from configparser import MAX_INTERPOLATION_DEPTH
from msilib.schema import Property
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Book(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Slot(models.Model):

    class BookGenre(models.TextChoices):
        FICTION = 'Fiction'
        NONFICTION = 'Nonfiction'
        DRAMA = 'Drama'
        POETRY = 'Poetry'
        FOLKTALE = 'Folktale'

    topic = models.CharField(
        max_length=20,
        choices=BookGenre.choices,
        null=True,
        blank=True
    )

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    #club people
    updated = models.DateTimeField(auto_now=True) #when affected
    created = models.DateTimeField(auto_now_add=True) #intial time 

    def __str__(self):
        return str(self.book)


    class Meta:
        ordering = ['-updated', '-created']
    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True) 
    body = models.TextField() 
    updated = models.DateTimeField(auto_now=True) #when affected
    created = models.DateTimeField(auto_now_add=True) #intial time 

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.body[0:50])

