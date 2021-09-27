"""simulation_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from houses_app import views

router = routers.DefaultRouter()
router.register(r'addresses', views.AddressView, 'addresses')
router.register(r'cities', views.CityView, 'cities')
router.register(r'countries', views.CountryView, 'countries')
router.register(r'houses', views.HouseView, 'houses')

# from houses_app.views import houses_list, find_house, create_house, update_house, delete_house

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('houses/', houses_list, name='houses-list'),
    # path('houses/<int:id>', find_house, name='find-house'),
    # path('houses/', create_house, name='create-house'),
    # path('houses/<int:id>', update_house, name='update-house'),
    # path('houses/<int:id>', delete_house, name='delete-house')
]
