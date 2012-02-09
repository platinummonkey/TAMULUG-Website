from django.forms import *
from django.forms.widgets import *
from tamulug.meetings.models import Meeting, Topic

class MeetingFormAdmin(ModelForm):
  '''Event form for creating meetings'''
  class Meta:
    model = Meeting # default model
    exclude = ('pub_date', 'publisher')

