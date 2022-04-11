from .authorModels import Author
from .authorSerializer import AuthorSerializer
from rest_framework import generics

# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class= AuthorSerializer
    
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class= AuthorSerializer