from django.test import TestCase
from datetime import datetime, date, time
from .models import MeetingMinutes, Meetings, Event, Resource
from .views import index, getmeeting, getmeetingdetails, getresource, newResource, newMeeting
from .forms import MeetingsForm, ResourceForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

# Create your tests here.
class MeetingsTest(TestCase):
    #SetUp Data
    def setUp(self):
        meeting= Meetings(meetingtitle="Villains Monthly", meetingdate= date(2021, 3, 12), meetingtime= time(3, 45), meetinglocation='Harley\'s Apartment', agenda='2')
        return meeting

    def test_string(self):
        meet = self.setUp()
        self.assertEqual(str(meet), meet.meetingtitle)

    #tests date - so that it is returning the right data type and the right string
    def test_date(self):
        meet=self.setUp()
        self.assertEqual(meet.meetingdate.strftime("%m/%d/%Y"), '03/12/2021') #Learned that strftime the small 'y' only returns the last two of the year. the large Y returns all four.
    
    def test_type(self):
        meet=self.setUp()
        self.assertEqual(meet.meetingdate, date(2021, 3, 12))
    
    def test_table(self):
        self.assertEqual(str(Meetings._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        meet=Meetings.objects.create(meetingtitle='Hero Coding', meetingdate=date(2021, 5, 5), meetingtime=time(3, 30), meetinglocation="Secret Base", agenda="Role, Updates, New Projects, Old Project, Adjourn")
        meetminutes = MeetingMinutes.objects.create(meetingID= meet, minutestext="To be entered after meeting secured") 
        return meetminutes
    
    def test_string(self):
        minutes = self.setUp()
        self.assertEqual(str(minutes), minutes.meetingID.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self, newuser='ivy'):
        u=User.objects.create(username= newuser)
        resource=Resource.objects.create(resourcename="Python for Dummies", resourcedate=date(2020, 12, 24), resourcetype='website', resourcedesc="Book for beginners working with Python. Good examples", UserID=u)
        return resource
    
    def test_string(self):
        resourcetest = self.setUp('bizzarro')
        self.assertEqual(str(resourcetest), resourcetest.resourcename)
    
    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    

class GetMeetingTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

class GetMeetingDetailsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='alfed')
        self.u2=User.objects.create(username='commish')
        self.u3=User.objects.create(username='serena')
        self.meet=Meetings.objects.create(meetingtitle='Support Characters: Code 4 Helping', meetingdate=date(2021, 4, 4), meetingtime=time(6), meetinglocation="Wayne Manor", agenda="Role, Updates, New Projects, Old Project, Adjourn")
        self.minutes = MeetingMinutes.objects.create(meetingID=self.meet, minutestext="We joined up to create a basic program to optimize the social events and sleep schedule for Mr. Wayne") 
        self.minutes.attendance.add(self.u,self.u2, self.u3)

    def test_minutes_attendance_success(self):
        response = self.client.get(reverse('meetingdetails', args=(self.meet.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_attendance_count(self):
        attendance=self.minutes.attendance.count()
        self.assertEqual(attendance, 3)

#Form Tests
class NewMeeting_Form_Test(TestCase):
    def test_meetingsform_is_valid(self):
        form=MeetingsForm(data={'meetingtitle': "Unit Tests for Police Apps", 'meetingdate': date(2021, 4, 24), 'meetingtime': time(17), 'meetinglocation': "Gordon\'s office", 'agenda': "Roll Call, Past problems, Guest Speaker, Adjourn"})
        self.assertTrue(form.is_valid())
    
    def test_meetingsform_No_Agenda(self):
        form=MeetingsForm(data={'meetingtitle': "Unit Tests for Police Apps", 'meetingdate': date(2021, 4, 24), 'meetingtime': time(17), 'meetinglocation': "Gordon\'s office"})
        self.assertTrue(form.is_valid())

    def test_meetingsform_empty(self):
        form=MeetingsForm(data={'meetingtitle': ""})
        self.assertFalse(form.is_valid())

    def test_meetingsform_nodate(self):
        form=MeetingsForm(data={'meetingtitle': "Unit Tests for Police Apps", 'meetingdate': ""})
        self.assertFalse(form.is_valid())

class NewMeeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuserPOW', password='P@ssword!')
        self.meeting=Meetings.objects.create(meetingtitle='Villains: Code 4 Chaos', meetingdate=date(2021, 6, 6), meetingtime=time(6,6), meetinglocation="Dive Bar", agenda="meh...")
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newmeeting/')
    
    def test_logged_in_uses_correct_template(self):
        login=self.client.login(username='testuserPOW', password='P@ssword!')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuserPOW')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newmeeting.html')