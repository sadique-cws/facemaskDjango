
from django.contrib import admin
from django.urls import path
from social.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage,name="homepage"),
    path("index/", index, name="index"),
    path("profile/", profile, name="profile"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path('post/new/', insert_post, name="insertPost"),
    path('upload-dp/', uploadDp, name="uploadDp"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


