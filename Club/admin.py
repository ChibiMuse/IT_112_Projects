from django.contrib import admin
from .models import Meetings, Resource, MeetingMinutes, Event

# Register your models here.
admin.site.register(Meetings)
admin.site.register(Resource)
admin.site.register(MeetingMinutes)
admin.site.register(Event)
