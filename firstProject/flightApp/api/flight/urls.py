from django.urls import path, include
from .flightView import FlightViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights', FlightViewSet)
urlpatterns = [
    path('/',include(router.urls))
]