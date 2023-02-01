from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=5, choices=GENDER)
    dp = models.ImageField(upload_to="dp/", blank=True, null=True)

    def __str__(self):
        return self.user.username
    



class Post(models.Model):
    post_by = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="post/",null=True,blank=True)

    def __str__(self):
        return self.post_by.username
    