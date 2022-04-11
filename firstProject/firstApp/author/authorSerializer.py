from .authorModels import Author
from ..book.bookSerializer import BookSerializer
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True,many=True)
    class Meta:
        model = Author
        fields='__all__'
