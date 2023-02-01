from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account,Post
from django.contrib.auth import authenticate, login as LoginFunction, logout as LogoutFunction
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.

def homepage(r):
    return render(r, "landing.html")

def index(r):
    return render(r, "index.html")

def login(r):
    if r.method == "POST":
        username = r.POST.get('email')
        password = r.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            LoginFunction(r, user)
            return redirect(profile)
        else:
            return redirect(homepage) 

        

    return render(r, "login.html")

def register(r):
    if r.method == "POST":
        # user
        u = User()
        u.first_name = r.POST.get('fname')
        u.last_name = r.POST.get('lname')
        u.email = r.POST.get('email')
        u.username = r.POST.get('username')
        u.set_password(r.POST.get("password"))
        u.is_active  = True
        u.is_staff = True
        u.save()

        # account record creation
        a = Account()
        a.user = u
        a.gender = r.POST.get('gender')
        a.dob = r.POST.get("dob")
        a.contact = r.POST.get('contact')
        a.save()
        LoginFunction(r,u)
        
        return redirect(profile)


@login_required()
def profile(r):
    data = {}
    data['posts'] = Post.objects.order_by("-id")
    return render(r, "profile.html",data)

def logout(r):
    LogoutFunction(r)
    return redirect(homepage)

def insert_post(r):
    if r.method == "POST":
        p = Post()
        user = User.objects.get(pk=r.user.id)
        p.post_by = user 
        p.caption = r.POST.get('caption')
        p.save()
        return redirect(profile)



def uploadDp(r):
    if r.method == "POST":
        user = User.objects.get(pk=r.user.id)
        file = r.FILES['dp']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        upload_file_url = fs.url(filename)
        user.dp = filename
        user.save()
        return redirect(profile)
