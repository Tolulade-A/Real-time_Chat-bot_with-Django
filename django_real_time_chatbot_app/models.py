from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000) #room name

class Message(models.Model):
    value = models.CharField(max_length=1000000) #message value/message of each user
    date = models.DateTimeField(default=datetime.now, blank=True) #date time of message occurence
    user = models.CharField(max_length=1000000) # the user
    room = models.CharField(max_length=1000000) #to identify the room the message is being sent to

    #then we makemigrations & migrate to the DB & create SU
    #then admin to import models

