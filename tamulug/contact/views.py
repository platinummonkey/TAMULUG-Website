from django.template import RequestContext
from django.shortcuts import render_to_response
from tamulug.contact.forms import ContactForm

from tamulug.meetings.utils import getNextMeeting

def contact(request={}):
  ''' Contact'''
  if request.POST:
    form = ContactForm(request.POST)
    if form.is_valid():
      cs = form.save() # sends emails
      return render_to_response('contact/thankyou.html', {'submission': cs, 'upcoming': getNextMeeting()}, context_instance=RequestContext(request))
  else:
    form = ContactForm()
  return render_to_response('contact/form.html', {'form': form, 'upcoming': getNextMeeting()}, context_instance=RequestContext(request))
