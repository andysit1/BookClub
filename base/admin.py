from django.contrib import admin

# Register your models here.
from .models import Book, Slot, Blog

admin.site.register(Book)
admin.site.register(Slot)
admin.site.register(Blog)