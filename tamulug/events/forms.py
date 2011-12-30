from django.forms import *
from django.forms.widgets import *
from tamulug.events.models import Event

class EventFormAdmin(ModelForm):
  '''Event form for creating meetings, and other events'''
  class Meta:
    model = Event # default model
    exclude = ('pub_date', 'publisher')

