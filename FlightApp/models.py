from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimateTimeOfDeparture = models.TimeField()



class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
