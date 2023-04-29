from rest_framework import generics

from events.serializers import *


# работа с мероприятием


class EventsView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class ListEventsViewOfTeam(generics.ListAPIView):
    """ вывод всех мероприятий, в которых команда участвует """
    serializer_class = EventSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        team_pk = self.kwargs['pk']
        teams = Team.objects.filter(id_system_team=team_pk)
        ivents = []
        for t in teams:
            ivents.append(Event.objects.get(pk=t.ivent_id))
        return ivents


#  региональные партнёры

class RegionalPartnerView(generics.CreateAPIView):
    serializer_class = RegionalPartnerSerializer


class RegionalPartnersView(generics.ListAPIView):
    serializer_class = TeamSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Team.objects.filter(pk=pk)


# команды


class TeamView(generics.CreateAPIView):
    serializer_class = TeamSerializer


class TeamViewList(generics.ListAPIView):
    serializer_class = TeamSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Team.objects.filter(pk=pk)


