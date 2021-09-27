from rest_framework import serializers
from .models import Address, City, Country, House

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'country')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address1', 'address2', 'city', 'zipcode', 'state')

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('property_name', 'mortgage_amount', 'desired_rent', 'address')
