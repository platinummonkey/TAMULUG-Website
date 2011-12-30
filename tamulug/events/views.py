import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from tamulug.events.models import Event
from tamulug.events.forms import *

def getSemesterRanges():
  year = datetime.datetime.now().year
  dd = datetime.datetime
  SEMESTER_RANGES = {'spring': (dd(year,1,1),  dd(year,5,20,23,59,59)),
                     'summer': (dd(year,5,21), dd(year,8,1,23,59,59)),
                     'fall':   (dd(year,8,2),  dd(year,12,31,23,59,59))}
  return SEMESTER_RANGES

def getCurrentSemester():
  today = datetime.datetime.now()
  ranges = getSemesterRanges()
  for k, r in ranges.items():
    if today >= r[0] and today <= r[1]:
      return (k, r)
   # something is wrong if you hit this! check your semester dates! as there should be no gaps
  return None

def index(request):
  curSem = getCurrentSemester()
  meetings = Event.objects.all().filter(meeting=True, event_date__gte=curSem[1][0]).filter(event_date__lte=curSem[1][1])
  return render_to_response('events/index.html', {'events': meetings}, context_instace=RequestContext(request))

def upcomingMeetings(request):
  today = datetime.datetime.today()
  curSem = getCurrentSemester()
  meetings = Event.objects.all().filter(meeting=True, event_date__gte=today).filter(event_date__lte=curSem[1][1])
  return render_to_response('events/event_list.html', {'events': meetings}, context_instace=RequestContext(request))

def nextMeeting(request):
  today = datetime.datetime.today()
  curSem = getCurrentSemester()
  # ordered by event date so the first in the QuerySet should be the next meeting
  meetings = Event.objects.all().filter(meeting=True, event_date__gte=today).filter(event_date__lte=curSem[1][1])[0]
  return render_to_response('events/next_event.html', {}, context_instace=RequestContext(request))

def allMeetings(request):
  meetings = Event.objects.all().filter(meeting=True)
  return render_to_response('events/event_list.html', {'events': meetings}, context_instace=RequestContext(request))

