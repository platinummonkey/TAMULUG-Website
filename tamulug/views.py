import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from tamulug.meetings.utils import getNextMeeting

def index(request):
  upcoming = getNextMeeting()
  return render_to_response('index.html', {'upcoming': upcoming}, context_instance=RequestContext(request))

