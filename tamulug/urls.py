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
    (r'^officers/', include('tamulug.accounts.urls-officers')),
    # meetings
    (r'^meetings/', include('tamulug.meetings.urls')),
    # contact us
    (r'^contact/', 'tamulug.contact.views.contact'),
    # tamulinux
    #(r'^tamulinux/', 'tamulug.views.tamulinux'),
    # irc
    (r'^irc/etiquette/', 'tamulug.views.irc_etiquette'),
    (r'^irc/', 'tamulug.views.irc'),
    # forum
    #(r'^forum/', include('tamulug.forum.urls')),
    # catpcha
    (r'^captcha/', include('captcha.urls')),

    # favicon.ico
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/site_images/favicon.ico'}),
)
