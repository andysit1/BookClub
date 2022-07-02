from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.db.models import Q
from requests import request, session

from .models import Slot, Blog, Book
from django.contrib import messages

from .form import BlogForm, SlotForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
#GET https://www.googleapis.com/books/v1/volumes?q={search terms}


#login/Logout ---

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'does not exist!') #checks for exsiting usernames

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist!') #user is there, just wrongly wrote

    context = {'page':page}

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    page = 'register'

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('valid')
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'An error occured during sign up.')
    context = {'form':form, 'page':page}
    return render(request, 'base/login_register.html', context)


def homeView(request):
    slots = Slot.objects.all()
    blogs = Blog.objects.all()

    print(slots)

    context = {'slots':slots, 'blogs':blogs}
    return render(request, 'base/home.html', context)


@login_required(login_url='/login')
def roomView(request, pk):
    slot = Slot.objects.get(id=pk)

    blogs = slot.blog_set.all()

    context = {'slot':slot, 'blogs':blogs}

    return render(request, 'base/room.html', context)

@login_required(login_url='/login')
def editBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/blog/edit_blog.html', context)

@login_required(login_url='/login')
def addBlog(request, pk):
    slot = Slot.objects.get(id=pk)

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
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'base/blog/add_blog.html', context)

from package import r_id_scrap, get_data

@login_required(login_url='/login')
def addBook(request, pk):
    try:
        r_id_scrap(pk)
    except Exception:
        pass

    info = get_data('data')
    title = info.get('title')

    initial = {
        'host': request.user,
        'book_id': pk,
        'title':title
    }
    form = SlotForm(initial=initial)

    if request.method == "POST":
        form = SlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('form is invalid')

    context = {'form':form}
    return render(request, 'base/book/add-book.html', context)

@login_required(login_url='/login')
def deleteBook(request, pk):
    slot = Slot.objects.get(id=pk)
    context = {'slot':slot}

    if request.method == "POST":
        slot.delete()
        return redirect('home')
    return render(request, 'base/book/delete_book.html', context)

from package import r_scrap


@login_required(login_url='/login')
def selectBook(request):
    books = []
    id = []
    if request.method == "POST":
        source = request.POST['book_name']
        info = r_scrap(source)['items']
        for i in range(5):
            books.append(info[i])

    context = {'books':books, 'id':id}
    return render(request, 'base/book/select_book.html', context)
