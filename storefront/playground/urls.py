from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('hello/html', views.say_hello_html)
]