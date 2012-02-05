from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
  topic = models.CharField(max_length=256, help_text='What is the topic?')
  presenter = models.CharField(max_length=256, help_text='Who is presenting this talk?')

  class Meta:
    ordering = ['topic', 'presenter']

  def __unicode__(self):
    return '%s: %s' % (self.presenter, self.topic)

class Meeting(models.Model):
  title = models.CharField(max_length=256, help_text='Short descriptive title')
  date = models.DateTimeField(help_text='Meeting Date')
  details = models.TextField(max_length=3000, help_text='Describe the event')
  is_dinner = models.BooleanField(default=False, help_text='Is this a dinner meeting?')
  dinner_location = models.CharField(blank=True, max_length=256, help_text='Ex. Freebirds, College Station, TX - google maps generated automatically')
  topics = models.ManyToManyField(Topic)
  publisher = models.ForeignKey(User, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True, editable=False)

  class Meta:
    ordering = ['-date', 'title', '-pub_date']

  def __unicode__(self):
    return '%s - %s' % (self.date.strftime('%m/%d/%Y %H:%M'), self.title)

  def getTopics(self):
    return self.topics.all()
