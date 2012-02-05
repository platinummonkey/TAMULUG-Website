from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tamulug.meetings.views',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # semester meeting list
    (r'^$', 'index'),
    # upcoming meeting list only
    #(r'^upcoming/$', 'upcomingMeetings'),
    # next meeting only
    #(r'^next/$', 'nextMeeting'),
    # all meetings
    #(r'^all/$', 'allMeetings'), # includes search capability
)
