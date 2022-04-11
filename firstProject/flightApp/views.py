from django.shortcuts import render
from .api.flight.flightModel import Flight
from .api.passenger.passengerModel import Passenger
from .api.reservation.reservationModel import Reservation
from .api.flight.flightSerializer import FlightSerializer
from .api.reservation.reservationSerializer import ReservationSerializer
from .api.passenger.passengerSerializer import PassengerSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import status

# Create your views here.
@api_view(['GET','POST'])
def reservation_operations(request):

    if request.method =='GET':
        flight = Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
        serializer=FlightSerializer(flight,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departureCity', 'arrivalCity','dateOfDeparture']



class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
