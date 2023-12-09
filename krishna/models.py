from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="krishna")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="maharashtra")
    country = models.CharField(max_length=50,default="india")
    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username

class Stations(models.Model):
    S_id = models.IntegerField(primary_key=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Latitude = models.CharField(max_length=10, null=True, blank=True)
    Longitude = models.CharField(max_length=10, null=True, blank=True)
    City = models.CharField(max_length=10, null=True, blank=True)
    State = models.CharField(max_length=10, null=True, blank=True)
    Country = models.CharField(max_length=10, null=True, blank=True)


class Slots(models.Model):
    S_id = models.ForeignKey(Stations, on_delete=models.CASCADE, default=None)
    booking_date=models.DateField(null=True, blank=True)
    slot1=models.BooleanField(default=False,null=True, blank=True)
    slot2=models.BooleanField(default=False,null=True, blank=True)
    slot3=models.BooleanField(default=False,null=True, blank=True)
    slot4=models.BooleanField(default=False,null=True, blank=True)
    slot5=models.BooleanField(default=False,null=True, blank=True)
    slot6=models.BooleanField(default=False,null=True, blank=True)
    slot7=models.BooleanField(default=False,null=True, blank=True)
    slot8=models.BooleanField(default=False,null=True, blank=True)
    slot9=models.BooleanField(default=False,null=True, blank=True)
    slot10=models.BooleanField(default=False,null=True, blank=True)
    slot11=models.BooleanField(default=False,null=True, blank=True)
    slot12=models.BooleanField(default=False,null=True, blank=True) 
    class Meta:
        unique_together = (('S_id', 'booking_date'),)
