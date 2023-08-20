from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    # Add any other fields needed for farmers and customers
class Items(models.Model):

    name=models.CharField(max_length=100)
    payment=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.DecimalField(max_digits=10,decimal_places=2)
    picture=models.ImageField(null=True,blank=True,upload_to='static/')


    def __str__(self):
        return self.name
class billing(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zip_code=models.DecimalField(max_digits=5,decimal_places=0)


    def __str__(self):
        return self.name

class Loan(models.Model):
    name=models.CharField(max_length=100)
    email=models.TextField()
    sop=models.TextField()
    ask_amount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name