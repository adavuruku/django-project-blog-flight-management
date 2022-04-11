# Create your models here.
from django.db import models
from ..customer.customerModel import Customer

class Order(models.Model):
    product=models.CharField(max_length=240)
    quantity=models.DecimalField(max_digits=8, decimal_places=2)
    customer= models.ForeignKey(Customer,related_name='orders',on_delete=models.CASCADE)