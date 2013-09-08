from django.conf.urls import *

urlpatterns = patterns('tamulug.accounts.views-officers',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # semester meeting list
    (r'^$', 'index'),
    # upcoming meeting list only
    #(r'^upcoming/$', 'upcomingMeetings'),
    # next meeting only
    #(r'^next/$', 'nextMeeting'),
    # all meetings
)
