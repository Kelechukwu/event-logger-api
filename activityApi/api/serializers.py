import time

from rest_framework import serializers
from .models import Event


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))

class EventPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    createdAt = TimestampField()
    class Meta:
        model = Event
        fields = '__all__'
