from django.db import models
from .author.authorModels import Author
from .book.bookModels import Book

from .customer.customerModel import Customer
from .order.orderModel import Order

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    sal = models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return self.id+self.name+self.sal

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return self.id+self.name+self.score

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField()
    rating = models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return self.id+self.title+self.rating