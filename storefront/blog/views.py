from operator import truediv
from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS
from .serializers import PostSerializer, RegisterUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class PostUserWritePermission(BasePermission):
    message = 'Editing restricted'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            print(request.user)
            return obj.author == request.user

        print(request.user)
        return obj.author == request.user

class OpenPost(generics.RetrieveAPIView):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset =  Post.postobjects.all()
    serializer_class = PostSerializer

class List(generics.ListAPIView, PostUserWritePermission):
    # permission_classes = [IsAdminUser]
    permission_classes = [PostUserWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class Post(generics.CreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(reg_serializer.data,status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)