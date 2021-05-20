from django.db import models

# Create your models here.

class contactinfo(models.Model):
    first_name=models.CharField(max_length=10);
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=15,default="")
    comment = models.CharField(max_length=200)


class booknow(models.Model):
    name = models.CharField(max_length=10);
    email = models.CharField(max_length=50,default="")
    mobile = models.CharField(max_length=15,default="")
    city = models.CharField(max_length=50,default="")
    state = models.CharField(max_length=50,default="")
    comment = models.CharField(max_length=50,default="")