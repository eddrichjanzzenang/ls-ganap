from main_events.models import Event
from main_events.serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
# import the pagination settings
from main_events.pagination import ObjectLimitOffsetPagination, ObjectPageNumberPagination
from rest_framework import status
# import Query lookups
from django.db.models import Q
from django.http import Http404
from datetime import datetime, timedelta
from rest_framework.filters import SearchFilter, OrderingFilter
from main_events.swagger import SimpleFilterBackend
from rest_framework.schemas import AutoSchema
import coreapi, coreschema

class FilterEventsBetweenDates(generics.ListAPIView):
    """
    get: Gets all events between a start_date and an end_date.
    """
    serializer_class = EventSerializer
    pagination_class = ObjectPageNumberPagination

    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "start_date",
            required=True,
            location="query",
            description='Specify a date in YYYY-MM-DD as the start of the range of dates.',
            schema=coreschema.String()
        ),
        coreapi.Field(
            "end_date",
            required=True,
            location="query",
            description='Specify a date in YYYY-MM-DD as the end of the range of dates, inclusive.',
            schema=coreschema.String()
        ),
    ])

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(hours=23, minutes=59, seconds=59, milliseconds=59)

        queryset = Event.objects.all()

        return get_dates_between(start_date, end_date, queryset, Event.start_time)

# helper method for getting date range
def get_dates_between(start_date, end_date, queryset, start_time):
    if(start_date is not None) and (end_date is not None):
        queryset = queryset.filter(start_time__range=[start_date, end_date]).order_by('start_time')
    else:
        raise Http404

    return queryset

class FilterEventByDate(generics.ListAPIView):
    """
    get: Gets all events given a specific date.
    """
    serializer_class = EventSerializer
    pagination_class = ObjectPageNumberPagination

    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "date",
            required=True,
            location="path",
            description='Specify a date in YYYY-MM-DD to get all the events held on the same date.',
            schema=coreschema.String()
        ),
    ])

    def get_queryset(self):
        date = self.kwargs['date']
        queryset = Event.objects.all()
        
        if date is not None:
            queryset = queryset.filter(start_time__date=date)

        return queryset

class FilterEventByWeek(generics.ListAPIView):
    """
    get: Gets all the events happening in the week of the date input, 
    where the week is Monday-Sunday.
    """
    serializer_class = EventSerializer
    pagination_class = ObjectPageNumberPagination

    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "date",
            required=True,
            location="path",
            description='Specify a date in YYYY-MM-DD to get all the events held in the same week.',
            schema=coreschema.String()
        ),
    ])

    def get_queryset(self):
        date = self.kwargs['date']
        get_date = datetime.strptime(date, '%Y-%m-%d')
        get_day = get_date.weekday()
        start_date = (get_date - timedelta(days=get_day))
        end_date = (get_date + timedelta(days=(6-get_day)))
        end_date = end_date + timedelta(hours=23, minutes=59, seconds=59, milliseconds=59)

        queryset = Event.objects.all()

        return get_dates_between(start_date, end_date, queryset, Event.start_time)

class FilterEventByMonth(generics.ListAPIView):
    """
    get: Gets all the events happening in the month of the input.
    """
    serializer_class = EventSerializer
    pagination_class = ObjectPageNumberPagination

    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "date",
            required=True,
            location="path",
            description='Specify a date in YYYY-MM-DD or in MM-YYYY to get all the events held in the same month.',
            schema=coreschema.String()
        ),
    ])

    def get_queryset(self):
        date = self.kwargs['date']
        try:
            get_month = datetime.strptime(date, '%Y-%m-%d').date().month
            get_year = datetime.strptime(date, '%Y-%m-%d').date().year
        except ValueError:
            date_list = date.split("-")
            get_month = date_list[0]
            get_year = date_list[1]

        queryset = Event.objects.all()

        if date is not None:
            queryset = queryset.filter(start_time__month=get_month, start_time__year=get_year)

        return queryset

class EventList(generics.ListCreateAPIView):
    """
    get: List all the events, ordered by start_time.
    post: Create a new event.
    """ 

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # specifies which pagination settings to follow
    pagination_class = ObjectPageNumberPagination
    serializer_class = EventSerializer
    filter_backends = [SearchFilter, OrderingFilter, SimpleFilterBackend]
    search_fields = ['name', 'venue_id__name', 'host_id__name']

    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "search",
            required=False,
            location="query",
            description='A search term for events with the given name, venue, or \
            host given the host_id.',
            schema=coreschema.String()
        ),
    ])

    # overwrite get_queryset() method
    def get_queryset(self, *args, **kwargs):
        queryset_list = Event.objects.all()
        query = self.request.GET.get("host_type_id")
        
        # only perform the filtering if the query has arguements
        # if not return all the events
        if query:
            queryset_list = queryset_list.filter(
                Q(host_id__host_type__id__contains=query)
            ).distinct()

        return queryset_list


    def list_items(self, request):
        """
        Return the list of events.
        """
        # make sure to filter by event start_time
        queryset = self.get_queryset().order_by('start_time')
        
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get: 
    Returns an event given its id
    
    put:
    Updates an event given its id

    patch:
    Updates an event given its id

    delete:
    Deletes an event given its id
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer





