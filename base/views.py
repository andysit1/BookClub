from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.db.models import Q
from .models import Slot, Blog, Book

from .form import BlogForm

def homeView(request):
    slots = Slot.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    books = slots.filter(
        Q(created__icontains=q) 
    )

    years = []

    for slot in slots:
        years.append(slot.created.year)
    
    for i, year in enumerate(years):
        if years[i] == years[i+1]:
            years.remove(years[i])
    print(years)
    
    context = {'slots':slots, 'years':years}
    return render(request, 'base/home.html', context)


def roomView(request, pk):
    slot = Slot.objects.get(id=pk)
    blogs = slot.blog_set.all()

    context = {'slot':slot, 'blogs':blogs}

    return render(request, 'base/room.html', context)

def createBook(request):

    context = {}
    return render(request, 'base/book_form.html', context)

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