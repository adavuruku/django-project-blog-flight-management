from django.db import models
from ..flight.flightModel import Flight
from ..passenger.passengerModel import Passenger


class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)