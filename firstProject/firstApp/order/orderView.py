from .orderModel import Order
from .orderSerializer import OrderSerializer
from rest_framework import generics

class OrderListView(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class= OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class= OrderSerializer