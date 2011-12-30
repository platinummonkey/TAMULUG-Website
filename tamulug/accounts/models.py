from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.ForeignKey(User, unique=True, related_name='profile')
  is_officer = models.BooleanField(default=False)
  officer_position = models.CharField(max_length=256, help_text='Officer Position title')
  officer_position_rank_order = models.IntegerField(default=10)
  get_meeting_emails = models.BooleanField(default=True)
  get_special_event_emails = models.BooleanField(default=True)

  def __unicode__(self):
    return self.user.get_full_name()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
