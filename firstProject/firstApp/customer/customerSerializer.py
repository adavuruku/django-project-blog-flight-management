from .customerModel import Customer
from ..order.orderSerializer import OrderSerializer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True,many=True)
    class Meta:
        model = Customer
        fields='__all__'