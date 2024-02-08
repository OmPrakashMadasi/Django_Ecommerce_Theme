from django.db import models
from django.contrib.auth.models import User
# from django.forms import ModelForm
# Create your models here.
from django.core.exceptions import ValidationError
import datetime
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Payment(models.Model):
    card_number = models.CharField(max_length=20)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=8, decimal_places=2)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'




