import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from tamulug.meetings.models import Meeting, Topic
from tamulug.meetings.utils import getCurrentSemesterMeetings, getNextMeeting
from tamulug.meetings.filterset import MeetingFilterSet
import csv

def index(request):
  meetings = getCurrentSemesterMeetings()
  print repr(meetings)
  upcoming = getNextMeeting()
  print repr(upcoming)
  return render_to_response('meetings/index.html',
         {'meetings': meetings, 'upcoming': upcoming},
         context_instance=RequestContext(request))

def getDownloadLink(request, type='csv'):
  dl = request.get_full_path().split('?')
  dl[0] = dl[0] + 'generate/%s/?' % type
  return ''.join(dl)


def filterAll(request, download=None):
  f = MeetingFilterSet(request.GET or None)
  numMeetings = f.qs.count()
  csvDownloadLink = getDownloadLink(request,'csv')

  if download == 'csv':
    # generate CSV for download
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=meeting_query_%s.csv' % datetime.datetime.now().strftime('%m%d%Y_%H%M')
    writer = csv.writer(response)
    writer.writerow(['Date','Title','Dinner (T/F)','Details','Topics','Presenters'])
    for m in f.qs:
      meetingTopics = m.topics.all()
      topics, presenters  = ([],[])
      if meetingTopics:
        for topic in meetingTopics:
          topics.append(topic.topic)
          presenters.append(topic.presenter)
      if topics:
        topics = '\n'.join(topics)
        presenters = '\n'.join(presenters)
      else:
        topics, presenters = ('', '')
      writer.writerow([str(m.date),str(m.title),str(m.is_dinner),str(m.details).replace(',',''),topics,presenters])
    return response
  return render_to_response('meetings/search.html', {'filter': f, 'numMeetings': numMeetings, 'csvDownloadLink', csvDownloadLink}, context_instance=RequestContext(request))
