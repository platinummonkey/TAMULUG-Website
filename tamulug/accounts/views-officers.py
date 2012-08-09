import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.models import User # django-builtin
from tamulug.accounts.models import UserProfile

from tamulug.meetings.utils import getNextMeeting

def index(request):
  officers = UserProfile.objects.all().filter(is_officer=True, user__is_active=True).order_by('officer_position_rank_order','officer_position','user__first_name')
  OFFICERS = [(o.user, o) for o in officers]
  return render_to_response('officers.html', {'officers': OFFICERS, 'upcoming': getNextMeeting()}, context_instance=RequestContext(request))
