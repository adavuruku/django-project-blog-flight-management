from django.urls import path, include
from .passengerView import PassengerViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('passengers', PassengerViewSet)
urlpatterns = [
    path('/',include(router.urls))
]