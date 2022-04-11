from django.urls import path, include
from firstApp import views
from django.contrib import admin
from django.urls import path
from .book import bookView
from .author import authorView
from .customer import customerView
from .order import orderView

# from firstApp.views import student_list, student_detail

"""
# function base components urls

urlpatterns = [
    path('emps/',views.employeeView),
    path('students',views.student_list),
    path('students/<int:pk>',views.student_detail)
]
"""

# class base view urls
urlpatterns = [
    path('students',views.StudentList.as_view()),
    path('students/<int:pk>',views.StudentDetail.as_view()),
    path('course',views.CourseList.as_view()),
    path('course/<int:pk>',views.CourseDetail.as_view()),

    path('course1',views.CourseListMixing.as_view()),
    path('course1/<int:pk>',views.CourseDetailMixing.as_view())
]

# viewset url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students-viewset',views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



urlpatterns = [
    path('author',authorView.AuthorListView.as_view()),
    path('author/<int:pk>',authorView.AuthorDetailView.as_view()),
    path('book',bookView.BookListView.as_view()),
    path('book/<int:pk>',bookView.BookDetailView.as_view()),
]

urlpatterns = [
    path('customer',customerView.CustomerListView.as_view()),
    path('customer/<int:pk>',customerView.CustomerDetailView.as_view()),
    path('order',orderView.OrderListView.as_view()),
    path('order/<int:pk>',orderView.OrderDetailView.as_view()),
]