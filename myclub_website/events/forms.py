from django import forms
from .models import Venue, Event

class VenueForm(forms.ModelForm):
  class Meta:
    model = Venue
    fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address', 'venue_image')
    
    #modify the labels in this example we make them empty
    labels = {
      'name':'', 
      'address':'', 
      'zip_code':'', 
      'phone':'', 
      'web':'', 
      'email_address':'',
      'venue_image':'',
    }

  #for styling using bootstrap all that class are bootstrap class
    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}), 
      'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), 
      'zip_code':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), 
      'phone':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}), 
      'web':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web'}), 
      'email_address':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    }


#admin superuser form
class AdminEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ('name', 'event_date', 'Venue', 'manager', 'attendees', 'description')
    labels = {
      'name':'', 
      'event_date':'YYYY-MM-DD HH:MM:SS', 
      'Venue':'Venue', 
      'manager':'manager', 
      'attendees':'attendees', 
      'description':''
      
      }
    
    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}), 
      'event_date':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'event_date'}), 
      'Venue':forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}), 
      'manager':forms.Select(attrs={'class': 'form-select', 'placeholder': 'manager'}), 
      'attendees':forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'attendees'}),
      'description':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
    }


#rigular user form
class UserEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ('name', 'event_date', 'Venue', 'attendees', 'description')
    labels = {
      'name':'', 
      'event_date':'YYYY-MM-DD HH:MM:SS', 
      'Venue':'Venue', 
      'attendees':'attendees', 
      'description':''
      
      }
    
    widgets = {
      'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}), 
      'event_date':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'event_date'}), 
      'Venue':forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),  
      'attendees':forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'attendees'}),
      'description':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
    }