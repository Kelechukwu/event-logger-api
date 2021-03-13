from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db.models import Q

from .serializers import EventSerializer, EventPOSTSerializer
from .models import Event
from .utils import parse_query_string

class EventView(APIView):

    def get_queryset(self):
        """ 
        This function parses the query string(if any) and
        returns : QueryList
        """
        queryset_list = Event.objects.all()
        query = self.request.GET.get('q')
        if query:
            parsed_query = parse_query_string(query)
            queryset_list = queryset_list.filter(
                eval(parsed_query))
        return queryset_list

    def post(self, request):
        """ Save an Event """
        serializer = EventPOSTSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            JsonResponse('An error occured',
                         status=status.HTTP_400_BAD_REQUEST, safe=False)

    def get(self, request):
        """ View Events """
        events = self.get_queryset()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)
