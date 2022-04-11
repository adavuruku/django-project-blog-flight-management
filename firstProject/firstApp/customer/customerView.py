from .customerModel import Customer
from .customerSerializer import CustomerSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
# LimitOffsetPagination allow the front end to specify the number of record they wan to load
class CustomPagination (PageNumberPagination):
    page_size = 10

class CustomerListView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class= CustomerSerializer
    # pagination_class = CustomPagination
    pagination_class = LimitOffsetPagination

    filter_backends = [filters.OrderingFilter]
    ordering = 'firstName' #default ordering
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['firstName','lastName', 'phone']
    # ^ starts with, = exact match, $ for regex

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['firstName','lastName', 'phone']
    
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class= CustomerSerializer