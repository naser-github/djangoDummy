from django.contrib import admin

from .models import Meetup
from .models import Location
from .models import Participant

# Register your models here.

class MeetUpAdmin(admin.ModelAdmin):
    list_display= ('title', 'date', 'location')
    list_filter = ('location','date')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Meetup, MeetUpAdmin)
admin.site.register(Location)
admin.site.register(Participant)