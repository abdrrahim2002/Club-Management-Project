from django.contrib import admin
from .models import Venue, MyClubUser, Event
from django.contrib.auth.models import Group
# Register your models here.

class VenuAdmin(admin.ModelAdmin):
  list_display = ['name', 'address', 'phone']
  ordering = ('name',)
  search_fields = ('name', 'address',)

admin.site.register(Venue, VenuAdmin)

class EventAdmin(admin.ModelAdmin):
  fields = (('name', 'Venue'), 'event_date', 'description', 'manager','approved')
  list_display = ['name', 'event_date', 'Venue']
  list_filter = ('event_date', 'Venue',)
  ordering = ('event_date',)

admin.site.register(Event, EventAdmin)

admin.site.register(MyClubUser)


#remove groups from admin page
admin.site.unregister(Group)

