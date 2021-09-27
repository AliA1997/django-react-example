from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CountrySerializer, CitySerializer, AddressSerializer, HouseSerializer
from .models import House, Country, City, Address

# Create your views here.

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class CountryView(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class HouseView(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()