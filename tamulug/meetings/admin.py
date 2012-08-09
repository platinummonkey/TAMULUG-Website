from django.contrib import admin
from tamulug.meetings.models import Meeting, Topic

class MeetingAdmin(admin.ModelAdmin):
  model = Meeting

class TopicAdmin(admin.ModelAdmin):
  model = Topic

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Topic, TopicAdmin)
