from django.db import models
from ..author.authorModels import Author

class Book(models.Model):
    title = models.CharField(max_length=20)
    ratings=models.CharField(max_length=10)
    author= models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)