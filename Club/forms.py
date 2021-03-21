from django import forms
from .models import Meetings, MeetingMinutes, Resource, Event


class MeetingsForm(forms.ModelForm):
    class Meta:
        model=Meetings
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'
    