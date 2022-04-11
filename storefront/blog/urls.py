from django.urls import path, include
from .views import Post, List, OpenPost, CustomUserCreate

urlpatterns = [
    path('<int:pk>/', OpenPost.as_view(), name='detailcreate'),
    path('new/', Post.as_view(), name='create'),
    path('', List.as_view(), name='list'),

    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('', List.as_view(), name='list'),

    path('user', CustomUserCreate.as_view(), name='createUser'),
]