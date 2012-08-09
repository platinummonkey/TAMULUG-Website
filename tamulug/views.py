import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from tamulug.meetings.utils import getNextMeeting
from random import randrange as random

def index(request):
  upcoming = getNextMeeting()
  return render_to_response('index.html', {'upcoming': upcoming}, context_instance=RequestContext(request))

def irc(request):
  upcoming= getNextMeeting()
  return render_to_response('irc.html', {'upcoming': upcoming, 'guest_name':'guest_'+str(random(0,99))}, context_instance=RequestContext(request))

def irc_etiquette(request):
  upcoming= getNextMeeting()
  return render_to_response('irc_etiquette.html', {'upcoming': upcoming}, context_instance=RequestContext(request))
