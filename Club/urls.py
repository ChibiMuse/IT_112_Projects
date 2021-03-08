from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('getmeeting/', views.getmeeting, name='meetings'),
   path('getresource/', views.getresource, name='resources'),
   path('meetingdetails/<int:id>', views.getmeetingdetails, name='meetingdetails'),
]
