from django.db import models

# Create your models here.

class House(models.Model):
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
class Cars(models.Model):
    first_name=models.CharField(max_length=20)   
    last_name=models.CharField(max_length=20) 

class Products(models.Model):
    name=models.CharField(max_length=30)
    original_price=models.CharField(max_length=30)
    discounted_price=models.CharField(max_length=30)
    image=models.ImageField(upload_to='products/')
