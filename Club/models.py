from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Meetings (meetingtitle, meetingdate, meeting time, location, agenda)
#Meeting Minutes (meeting id FK, attendance, minutes text)
#Resource (resource name, resource type, URL, date entered, USer ID FK, description)
#Event (event title, location, date, time, description, user ID)

class Meetings(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    agenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meetings, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingID
    
    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceURL=models.URLField(null=True, blank=True)
    resourcedate=models.DateField()
    UserID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedesc=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventlocation=models.CharField(max_length=255)
    eventuser=models.ManyToManyField(User)
    eventdesc=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'