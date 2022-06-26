from django.forms import ModelForm

from .models import Blog, Slot


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class SlotForm(ModelForm):
    class Meta:
        model = Slot
        fields = ['host', 'book_id', 'title']