from django.db import models

# Create your models here.
class Mrouter(models.Model):
    nama = models.CharField(max_length=40)
    host = models.CharField(max_length=40)
    user = models.CharField(max_length=40)
    password = models.CharField(max_length=50,blank=True)
    up_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nama
    
class Router(models.Model):
    nama = models.CharField(max_length=40)
    host = models.CharField(max_length=40)
    user = models.CharField(max_length=40)
    password = models.CharField(max_length=50,blank=True)
    up_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nama


