from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.db.models import Q
from .models import Slot, Blog, Book

from .form import BlogForm, SlotForm

from package import r_scrap, r_id_scrap

#GET https://www.googleapis.com/books/v1/volumes?q={search terms}

def homeView(request):
    slots = Slot.objects.all()
    context = {'slots':slots}
    return render(request, 'base/home.html', context)


def roomView(request, pk):
    slot = Slot.objects.get(id=pk)
    blogs = slot.blog_set.all()

    context = {'slot':slot, 'blogs':blogs}

    return render(request, 'base/room.html', context)


def editBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/edit_blog.html', context)

def addBlog(request, pk):
    slot = Blog.objects.get(id=pk)
    print(request.user)
    print(pk)
    initial = {
        'user': request.user,
        'slot':slot,
    }
    form = BlogForm(initial=initial)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form':form}
    return render(request, 'base/add_blog.html', context)


def addBook(request, pk):
    data = r_id_scrap(pk)
    
    initial = {
        'host': request.user,
    }
    form = SlotForm(initial=initial)
    if request.method == "POST":
        form = SlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
  
    context = {'form':form, 'book':data}
    return render(request, 'base/add-book.html', context)

def selectBook(request):
    books = []
    id = []
    if request.method == "POST":
        source = request.POST['book_name']
        info = r_scrap(source)['items']
        for i in range(5):
            books.append(info[i])
            
    context = {'books':books, 'id':id}
    return render(request, 'base/select_book.html', context)
