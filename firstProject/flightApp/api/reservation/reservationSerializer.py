from rest_framework import serializers
from .reservationModel import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'