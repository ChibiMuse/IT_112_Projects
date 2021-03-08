from django.shortcuts import render
from .models import Meetings, Resource, MeetingMinutes, Event

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def getmeeting(request):
    meeting_list=Meetings.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list' : meeting_list})

def getresource(request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resources.html' , {'resource_list' : resource_list})
