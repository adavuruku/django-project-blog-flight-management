# Create your models here.
from django.db import models
# from ..order.orderModel import Order

class Customer(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    phone=models.CharField(max_length=11)
    # orders = models.ManyToManyField(Order)
    # orders= models.ForeignKey(Order,related_name='orders',on_delete=models.CASCADE)
