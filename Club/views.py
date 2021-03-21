from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Meetings, Resource, MeetingMinutes, Event
from .forms import MeetingsForm, ResourceForm

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

#form methods

def newMeeting(request):
    form=MeetingsForm
    if request.method=='POST':
        form=MeetingsForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingsForm()
    else:
        form=MeetingsForm()
    return render(request, 'Club/newmeeting.html', {'form': form})

def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'Club/newresource.html', {'form': form})
    
