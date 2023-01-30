
from django.contrib import admin
from django.urls import path
from social.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage,name="homepage"),
    path("index/", index, name="index"),
    path("profile/", profile, name="profile"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]
