from ..passenger.passengerModel import Passenger
from ..passenger.passengerSerializer import PassengerSerializer
from ..flight.flightModel import Flight
from ..flight.flightSerializer import FlightSerializer
from .reservationModel import Reservation
from .reservationSerializer import ReservationSerializer
from ..base.baseView import BaseView
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# class ReservationView(BaseView):
#     def __init__(self):
#         super().__init__(Reservation, ReservationSerializer)

# Create your views here.
@api_view(['POST'])
def reservation_operations(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.phone = request.data['phone']
    passenger.email = request.data['email']
    passenger.save()

    reservation= Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)
    # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer