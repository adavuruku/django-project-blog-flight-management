from .flightModel import Flight
from .flightSerializer import FlightSerializer
from ..base.baseView import BaseView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# class FlightView( BaseView, viewsets.ModelViewSet):
#     def __init__(self):
#         super().__init__(Flight, FlightSerializer)


# Create your views here.
@api_view(['GET'])
def reservation_operations(request):
    flight = Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FlightSerializer(flight,many=True)
    return Response(serializer.data)

# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departureCity', 'arrivalCity','dateOfDeparture']

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)