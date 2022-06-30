from django.db import models
from django.contrib.auth.models import User
from matplotlib.pyplot import title

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Slot(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book_id = models.CharField(max_length=60)

    #fill after scrap
    title = models.TextField(blank=True, null=True)

    updated = models.DateTimeField(auto_now=True) #when affected
    created = models.DateTimeField(auto_now_add=True) #intial time

    def __str__(self):
        return str(self.title)

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

