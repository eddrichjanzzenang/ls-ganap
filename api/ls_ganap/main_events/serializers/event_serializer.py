from rest_framework import serializers
from main_events.models import Event, EventLogistic, Tag, SangguHost, OfficeHost, OrgHost

class EventLogisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLogistic
        fields = ['date',
                'start_time', 
                'end_time',
                'venue']
    # def 

class EventLogisticSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLogistic
        fields = ['event',
                'date',
                'start_time', 
                'end_time',
                'venue']

class EventSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    event_logistics = EventLogisticSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 
                'name',
                'sanggu_hosts',
                'office_hosts',
                'org_hosts', 
                'description', 
                'poster_url', 
                'outside_venue_name',
                'event_url',
                'tags',
                'event_logistics']

class CreateEventSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ['id', 
                'name',
                'sanggu_hosts',
                'office_hosts',
                'org_hosts',
                'description', 
                'poster_url', 
                'outside_venue_name',
                'event_url',
                'tags']
                # 'event_logistics']
