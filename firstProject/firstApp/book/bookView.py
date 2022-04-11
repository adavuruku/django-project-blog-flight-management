from .bookModels import Book
from .bookSerializer import BookSerializer
from rest_framework import generics

class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer