from rest_framework import serializers
from .passengerModel import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields='__all__'