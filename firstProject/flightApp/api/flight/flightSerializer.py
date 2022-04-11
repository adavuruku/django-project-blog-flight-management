from wsgiref import validate
from rest_framework import serializers
from .flightModel import Flight
import re

def isFlightNumberValid(data):
    print("isFlightNumberValid")

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields='__all__'
        validators = [isFlightNumberValid]
    
    # validation logic for a specific field
    def validate_flightNumber(self, flightNumber):
        if(re.match("^[a-zA-Z0-9]*$", flightNumber)==None):
            raise serializers.ValidationError("Invalid Flight Number, Make sure it is alpha numeric")
        return flightNumber
        
    # validation logic for all fields 
    def validate(self, data):
        print("general validator")
        print(data['flightNumber'])
        return data