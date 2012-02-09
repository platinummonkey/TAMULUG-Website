from tamulug.meetings.models import Meeting
import datetime

def getSemesterRanges():
  year = datetime.datetime.now().year
  dd = datetime.datetime
  SEMESTER_RANGES = {'spring': (dd(year,1,1),  dd(year,5,31,23,59,59)),
                     'summer': (dd(year,6,1), dd(year,7,31,23,59,59)),
                     'fall':   (dd(year,8,1),  dd(year,12,31,23,59,59))}
  return SEMESTER_RANGES

def getCurrentSemester():
  today = datetime.datetime.now()
  ranges = getSemesterRanges()
  for k, r in ranges.items():
    if today >= r[0] and today <= r[1]:
      return (k, r)
   # something is wrong if you hit this! check your semester dates! as there should be no gaps
  return None

def getCurrentSemesterMeetings():
  curSem = getCurrentSemester()
  try:
    meetings = Meeting.objects.all().filter(date__gte=curSem[1][0], date__lte=curSem[1][1])
  except:
    meetings = None
  return meetings

def getNextMeeting():
  today = datetime.datetime.today()
  curSem = getCurrentSemester()
  # ordered by event date so the first in the QuerySet should be the next meeting
  try:
    nextMeeting = Meeting.objects.all().filter(date__gte=today, date__lte=curSem[1][1])[0]
  except:
    nextMeeting = None
  return nextMeeting

def getallMeetings():
  meetings = Meeting.objects.all()
  return meetings

