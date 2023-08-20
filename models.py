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


class Loan(models.Model):
    name=models.CharField(max_length=100)
    email=models.TextField()
    sop=models.TextField()
    ask_amount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name


class Billing(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.DecimalField(max_digits=5, decimal_places=0)

    transport_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def calculate_transport_cost(self):
        city_transport_costs = {
            "Dhaka": 2000,
            "Rajshahi": 15000,
            "Chittagong": 20000,
            "Sylhet":25000,
            "Barishal":15000,
            "Jassor":12000,
            "Khulna":10000,

        }

        if self.city in city_transport_costs:
            return city_transport_costs[self.city]
        else:
            return 0

    def save(self, *args, **kwargs):
        self.transport_cost = self.calculate_transport_cost()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
