from rest_framework import serializers

from events.models import Event, Team, RegionalPartner


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class RegionalPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalPartner
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'



