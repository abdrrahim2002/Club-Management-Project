from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from django.contrib.auth.models import User #import user model from django
from .forms import VenueForm, AdminEventForm, UserEventForm
import csv

#for pdf generation
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#for pagination
from django.core.paginator import Paginator

from django.contrib import messages

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
  if request.user.is_authenticated:
    firstname = request.user.username
  else:
    firstname = "User"
    
  month = month.title()

  #convert month name to number
  month_number = list(calendar.month_name).index(month)
  month_number = int(month_number)

  #create calendar
  calender = HTMLCalendar().formatmonth(year, month_number)

  #get current year
  now = datetime.now()
  cureent_year = now.year

  #Query the event Models for dates
  event_list = Event.objects.filter(
    event_date__year=year,
    event_date__month=month_number,
    )
  


  #get current time
  time = now.strftime('%I:%M %P')
  day = datetime.now().day
  return render(request, 'events/home.html',{
    'name': firstname,
    'year': year,
    'month': month,
    'day': day,
    'month_number': month_number,
    'calender': calender,
    'current_year': cureent_year,
    'time': time,
    'event_list': event_list,
  })

def all_events(request):
  event_list = Event.objects.all().order_by('-name', 'Venue')
  
  return render(request, 'events/event-list.html', {
    'event_list': event_list,
  })

def add_venue(request):
  submitted = False

  if request.method == 'POST':
    form = VenueForm(request.POST, request.FILES) #we add 'request.FILES' to deal with image Files
    if form.is_valid():
      venue = form.save(commit=False) # we use this to delay the saving
      venue.owner = request.user.id # this is the logged in user ID
      venue.save()
      return HttpResponseRedirect('/add-venue?submitted=True')
    
  else:
    form = VenueForm()
    if 'submitted' in request.GET:
      submitted = True

  return render(request, 'events/add-venue.html', {
    'form': form,
    'submitted': submitted
  })



def list_venues(request):
  #venue_list = Venue.objects.all().order_by('?') #we use '?' to randomiz show data
  venue_list = Venue.objects.all()

  #set up pagination
  pagination = Paginator(Venue.objects.all(), 2) #in Paginator put the data list and then the number of data per page
  page = request.GET.get('page') #this is the request
  venues = pagination.get_page(page)

  nums = 'a'*venues.paginator.num_pages #this for calculate how many pages we will get

  return render(request, 'events/venues.html', {
    'venue_list': venue_list,
    'venues': venues,
    'nums':nums
  })




def show_venue(request, venue_id):
  venue = Venue.objects.get(id=venue_id)
  venue_owner = User.objects.get(pk=venue.owner)
  
  #grab event from that venue
  events = venue.event_set.all()
  
  return render(request, 'events/show-venue.html', {
    'venue': venue,
    'venue_owner': venue_owner,
    'events': events,
  })




def search_venue(request):
  if request.method == 'POST':
    
    searched = request.POST.get('searched')
    venues = Venue.objects.filter(name__contains=searched)

    return render(request, 'events/search-venue.html', {
    'searched': searched,
    'venues': venues
    })

  else:
    return render(request, 'events/search-venue.html', {
    
    })
  

def update_venue(request, venue_id):
  venue = Venue.objects.get(id=venue_id)
  form = VenueForm(request.POST or None, request.FILES or None, instance=venue) #instance to set the data that are store 
  if form.is_valid():
    form.save()
    return redirect('list-venue')

  return render(request, 'events/update-venue.html',{
    'venue': venue,
    'form':form
  }) 

def delete_venue(request, venue_id):
  venue = Venue.objects.get(id=venue_id)
  venue.delete()
  return redirect('list-venue')

#generate text file venue list
def venue_text(request):
  response = HttpResponse(content_type='text/plain')
  response['Content-Disposition'] = 'attachement; filename=venues.txt'
  
  #designate the model
  venues = Venue.objects.all()
  
  #create blank list
  line = []

  #loop thru and output
  for venue in venues:
    line.append(f'{venue.name}\n{venue.address}\n{venue.phone}\n{venue.zip_code}\n{venue.web}\n{venue.email_address}\n\n\n')

  #write to textfile
  response.writelines(line)
  return response

#generate csv TABLE 'spredsheet' file venue list
def venue_csv(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachement; filename=venues.csv'

  #create a csv writer
  writer = csv.writer(response)
  
  #designate the model
  venues = Venue.objects.all()

  #add column headings to the csvfile
  writer.writerow(['Venue name', 'Address', 'phone', 'zip code', 'web address', 'email'])
  
  #loop thru and output
  for venue in venues:
    writer.writerow([venue.name, venue.address, venue.phone, venue.zip_code, venue.web, venue.email_address])

  #write to csv
  return response

#generate pdf file for venue list we have to istale 'reportlab' using pip
def venue_pdf(request):
  # Create ByteStream buffer
  buf = io.BytesIO()

  # Create a canvas
  canv = canvas.Canvas(buf, pagesize=letter, bottomup=0)

  # Function to set up the font and other settings consistently
  def setup_canvas(canv):
      canv.setFont('Helvetica-Bold', 20)
      canv.drawString(inch, inch - 20, 'Venue List')
      canv.setFont('Helvetica', 14)

  # Set up the first page
  setup_canvas(canv)

  # Vertical position for the text
  line_height = 18
  y_position = 1.5 * inch  # Start a bit further down from the title

  # Import data from the Venue model
  venues = Venue.objects.all()

  # Loop through venues and add them to the PDF
  for venue in venues:
      text = f"Name: {venue.name}\nAddress: {venue.address}\nZip Code: {venue.zip_code}\nPhone: {venue.phone}\nWebsite: {venue.web}\nEmail: {venue.email_address}"
      
      # Add venue information in blocks
      for line in text.split("\n"):
          canv.drawString(inch, y_position, line)
          y_position += line_height  # Move down for the next line
      
      # Add a separator between venues
      canv.drawString(inch, y_position, "------------------------------------")
      y_position += line_height + 10  # Additional spacing between venues

      # Check for page break
      if y_position > 10 * inch:  # If we are near the bottom of the page
          canv.showPage()  # Start a new page
          setup_canvas(canv)  # Reapply the font and settings for the new page
          y_position = 1.5 * inch  # Reset the y_position for the new page

  # Finish up
  canv.showPage()
  canv.save()

  # Go to the beginning of the buffer
  buf.seek(0)

  # Return the response with the PDF
  return FileResponse(buf, as_attachment=True, filename='venue.pdf')



def add_event(request):
  submitted = False
  if request.method == 'POST':
    if request.user.is_superuser:
      form = AdminEventForm(request.POST)
      #saving
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/add-event?submitted=True')
    else:
      form = UserEventForm(request.POST)

      if form.is_valid():
        event = form.save(commit=False)
        event.manager = request.user
        event.save()
        return HttpResponseRedirect('/add-event?submitted=True')
    
  else:
    if request.user.is_superuser:
      form = AdminEventForm
    else:
      form = UserEventForm
    
    if 'submitted' in request.GET:
      submitted = True

  return render(request, 'events/add-event.html', {
    'form':form,
    'submitted':submitted
  })

def update_event(request, event_id):
  event = Event.objects.get(id=event_id)
  if request.user.is_superuser: #or we can set it to request.user.id == 1 cuz the superuser ID is 1
    form = AdminEventForm(request.POST or None, instance=event)
  else:
    form = UserEventForm(request.POST or None, instance=event) #instance to set the data that are store 
  
  if form.is_valid():
    form.save()
    return redirect('list-events')

  return render(request, 'events/update-event.html',{
    'event': event,
    'form':form
  }) 

def delete_event(request, event_id):
  event = Event.objects.get(id=event_id)
  if request.user == event.manager:
    event.delete()
    messages.success(request, ('Event was deleted'))
    return redirect('list-events')
  else:
    messages.success(request, ('Your are not authorized to delete'))
    return redirect('list-events')


#create mu event page
def my_events(request):
  if request.user.is_authenticated:
    me = request.user.id #this return the current user ID
    MyEvents = Event.objects.filter(attendees=me) #filter the database

    return render(request, 'events/my-events.html',{
      'MyEvents':MyEvents,
    })
  else:
    messages.success(request, ("you don't have evensts or access denied"))
    return redirect('home')
  


def search_events(request):
  if request.method == 'POST':
    
    searched = request.POST.get('searched')
    events = Event.objects.filter(name__contains=searched)

    return render(request, 'events/search-events.html', {
    'searched': searched,
    'events': events
    })

  else:
    return render(request, 'events/search-events.html', {
    
    })
  

def admin_approval(request):
  #get the venues 
  venue_list = Venue.objects.all()

  #get accounts
  event_count = Event.objects.all().count()
  venue_count = Venue.objects.all().count()
  user_count = User.objects.all().count()

  #get the events list for checkbox
  event_list = Event.objects.all().order_by('-event_date')
  
  if request.user.is_superuser:
    if request.method == 'POST':
      id_list = request.POST.getlist('boxes')
      
      #we use this methode because of check boxes !!!
      #uncheck all evnets
      event_list.update(approved=False)

      #update the database
      for id in id_list:
        Event.objects.filter(pk=int(id)).update(approved=True)

      messages.success(request, "Update done!")
      return redirect('list-events')
    else:
      return render(request, 'events/admin-approval.html', {
        'event_list': event_list,
        'event_count': event_count,
        'venue_count': venue_count,
        'user_count': user_count,
        'venue_list': venue_list,
      })
    
  else:
    messages.success(request, "You aren't authorized to view this page")
    return redirect('home')
 
#show event
def show_event(request, event_id):
  event = Event.objects.get(pk=event_id)
  return render(request,'events/show-event.html',{
  'event':event,
  })

#show events in a venue 
def venue_event(request, venue_id):
  #grab the venue
  venue = Venue.objects.get(id=venue_id)

  #grab event from that venue
  events = venue.event_set.all()
  if events:
    return render(request,'events/venue-event.html',{
      'events':events,
    })
  else:
    messages.success(request, 'That venue has no event !!')
    return redirect('admin-approval')