from django.shortcuts import render, get_object_or_404, get_list_or_404
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

def getmeetingdetails(request, id):
    meet=get_object_or_404(Meetings, pk=id)
    date=meet.meetingdate
    time=meet.meetingtime
    location=meet.meetinglocation
    agenda=meet.agenda
    minutes=MeetingMinutes.objects.filter(meetingID=id)
    attend=MeetingMinutes.attendance.through.objects.all()
    context={
        'meet' : meet,
        'date' : date,
        'time' : time,
        'location' : location,
        'agenda' : agenda,
        'minutes' : minutes,
        'attend' : attend,

    }
    return render(request, 'Club/meetingdetails.html', context=context)
    
