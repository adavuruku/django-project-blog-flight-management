from rest_framework import serializers
from blog.models import Post
from playground.models import NewUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title',  'author', 'excerpt', 'content', 'status')

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name',  'password')
        extra_kwargs = {'password':{
            'write_only':True
        }}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance