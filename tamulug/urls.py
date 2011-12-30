from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tamulug/', include('tamulug.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # home page
    (r'^$', 'tamulug.views.index'),
    # current officers
    #(r'^officers/', include('tamulug.officers.urls')),
    # meetings
    #(r'^meetings/', include('tamulug.meetings.urls')),
    # contact us
    (r'^contact/', 'tamulug.views.contactus'),
    # tamulinux
    (r'^tamulinux/', 'tamulug.views.tamulinux'),
    # irc
    (r'^irc/', 'tamulug.views.webIRCclient'),
    # forum
    #(r'^forum/', include('tamulug.forum.urls')),
)
