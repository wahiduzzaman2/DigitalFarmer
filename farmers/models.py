from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Loan(models.Model):
    name=models.CharField(max_length=100)
    email=models.TextField()
    sop=models.TextField()
    ask_amount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name