from django.contrib import admin

from .models import Event
from .models import Participant
##Register the data generated by EventForm to admin panel
admin.site.register(Event)
admin.site.register(Participant)