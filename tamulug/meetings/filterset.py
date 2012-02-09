import django_filters
from tamulug.meetings.models import *
import datetime, time

class MeetingFilterSet(django_filters.FilterSet):
  title = django_filters.filters.CharFilter(lookup_type='icontains',label="Title")
  is_dinner = django_filters.filters.BooleanFilter(label="Search Dinners?")
  details = django_filters.filters.CharFilter(lookup_type='icontains',label="Details")
  date = django_filters.filters.DateFilter(label="Date")
  topic = django_filters.filters.CharFilter(lookup_type='icontains', name='topics__topic',label="Topics")
  presenter = django_filters.filters.CharFilter(lookup_type='icontains', name='topics__presenter',label="Presenters")

  class Meta:
    model = Meeting
    fields = ['date','title','details','is_dinner']
    order_by = True # allow any field to be sorted by

  def __init__(self, *args, **kwargs):
    super(MeetingFilterSet, self).__init__(*args, **kwargs)
    for name, field in self.filters.iteritems():
      if isinstance(field, django_filters.filters.ChoiceFilter):
        # Add 'Any' entry to choice fields
        field.extra['choices'] = tuple([('', 'Any'), ] + list(field.extra['choices']))
