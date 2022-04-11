from django.urls import path, include
from .reservationView import ReservationViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('reservations', ReservationViewSet)
urlpatterns = [
    path('/',include(router.urls))
]