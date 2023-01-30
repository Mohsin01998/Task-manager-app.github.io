from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50,null=True)
    content = models.CharField(max_length=100, null=True)
    date_pub=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,max_length=10)


class Profile(models.Model):
    profile_pic=models.ImageField(null=True,blank=True,default='default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, max_length=10)
