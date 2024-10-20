from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
	path('<int:year>/<str:month>/', views.home, name='home'),
  path('events', views.all_events, name='list-events'),
  path('add-venue', views.add_venue, name='add-venue'),
  path('list-venues', views.list_venues, name='list-venue'),
  path('show-venue/<venue_id>', views.show_venue, name='show-venue'),
  path('search-venue', views.search_venue, name='search-venue'),
  path('update-venue/<venue_id>', views.update_venue, name='update-venue'),
  path('delete-venue/<venue_id>', views.delete_venue, name='delete-venue'),
  path('add-event', views.add_event, name='add-event'),
  path('update-event/<event_id>', views.update_event, name='update-event'),
  path('delete-event/<event_id>', views.delete_event, name='delete-event'),
  path('venue-text', views.venue_text, name='venue-text'),
  path('venue-csv', views.venue_csv, name='venue-csv'),
  path('venue-pdf', views.venue_pdf, name='venue-pdf'),
  path('my-events', views.my_events, name='my-events'),
  path('search-events', views.search_events, name='search-events'),
  path('admin-approval', views.admin_approval, name='admin-approval'),
  path('venue-event/<venue_id>', views.venue_event, name='venue-event'),
  path('show-event/<event_id>', views.show_event, name='show-event'),
]
