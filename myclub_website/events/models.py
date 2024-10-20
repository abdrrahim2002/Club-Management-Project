from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Venue(models.Model):
  name = models.CharField('Venue Name', max_length=120)
  address = models.CharField(max_length=300)
  zip_code = models.CharField('Zip Code', max_length=20)
  phone = models.CharField('Contact Phone', max_length=30, blank=True)
  web = models.URLField('Website Address', blank=True)
  email_address = models.EmailField('Email', blank=True)
  owner = models.IntegerField('Venue owner', blank=False, default=1)
  venue_image = models.ImageField(null=True, blank=True, upload_to='images')


  def __str__(self):
    return self.name


class MyClubUser(models.Model):
  first_name = models.CharField('First Name', max_length=50)
  last_name = models.CharField('Last Name', max_length=50)
  email = models.EmailField('User Email')

  def __str__(self):
    return self.first_name + ' ' + self.last_name


class Event(models.Model):
  name = models.CharField('Event Name', max_length=150)
  event_date = models.DateTimeField('Event Date')
  Venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE) #connect the Venue table
  manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, max_length=150)
  description = models.TextField(blank=True)
  attendees = models.ManyToManyField(MyClubUser, blank=True)#connect MyClubUser to this table
  approved = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name


  #this is for calculate and return how many days left till the event start
  @property
  def Days_till(self):
    today = date.today()
    days_till = self.event_date.date() - today
    days_till_stripped = str(days_till).split(',', 1)[0]
    return days_till_stripped
  
  @property
  def Is_Past(self):
    today = date.today()
    if self.event_date.date() < today:
      event = 'Past'
    else:
      event = 'Future'

    return event