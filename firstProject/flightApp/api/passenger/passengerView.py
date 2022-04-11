from .passengerModel import Passenger
from .passengerSerializer import PassengerSerializer
from ..base.baseView import BaseView
from rest_framework import filters
from rest_framework import viewsets

# class PassengerView(BaseView):
#     def __init__(self):
#         super().__init__(Passenger, PassengerSerializer)

class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer