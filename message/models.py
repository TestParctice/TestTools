from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    ctime = models.DateField()
    utime = models.DateField()
    isDel = models.IntegerField(default=0)
