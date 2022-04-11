from django.urls import path, include
from .api.flight import flightView
from .api.reservation import reservationView
from .api.passenger import passengerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights',flightView.FlightViewSet)
router.register('reservations',passengerView.PassengerViewSet)
router.register('passengers',reservationView.ReservationViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/findFlights/',flightView.reservation_operations),
    path('api/v1/saveFlight/',reservationView.reservation_operations),
    # path('/',include('api.reservation.urls')),

]