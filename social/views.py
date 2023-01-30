from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account,Post
# Create your views here.

def homepage(r):
    return render(r, "landing.html")

def index(r):
    return render(r, "index.html")

def login(r):
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
        return redirect(homepage)


def profile(r):
    return render(r, "profile.html")

def logout(r):
    pass 
