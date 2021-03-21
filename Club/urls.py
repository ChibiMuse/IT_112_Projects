from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('getmeeting/', views.getmeeting, name='meetings'),
   path('getresource/', views.getresource, name='resources'),
   path('meetingdetails/<int:id>', views.getmeetingdetails, name='meetingdetails'),
   path('newmeeting/', views.newMeeting, name='newmeeting'),
   path('newresource/', views.newResource, name='newresource'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
