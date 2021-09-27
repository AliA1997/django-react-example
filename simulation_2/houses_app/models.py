from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}, {self.country.name}"

class Address(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.address1} {self.city.__str__} #{self.zipcode}"
    
class House(models.Model):
    property_name = models.CharField(max_length=200)
    mortgage_amount = models.BigIntegerField()
    desired_rent = models.BigIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return f"{property_name} {self.address.__str__} \n Mortgage Amount: {self.mortgage_amount} \n Desired Rent: {self.desired_rent}"