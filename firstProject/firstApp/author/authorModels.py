# Create your models here.
from django.db import models

class Author(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)