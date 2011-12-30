from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
  title = models.CharField(max_length=256, help_text='Short descriptive title')
  event_date = models.DateTimeField(help_text='Event Date')
  is_meeting = models.BooleanField(default=True, help_text='Is this a meeting?')
  details = models.TextField(max_length=3000, help_text='Describe the event')
  publisher = models.ForeignKey(User, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True, editable=False)

  class Meta:
    ordering = ['-event_date', 'title', '-pub_date']

  def __unicode__(self):
    return '%s - %s' % (self.event_date.strftime('%m/%d/%Y %H:%M'), self.title)

