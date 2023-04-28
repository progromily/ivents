from rest_framework import serializers

from ivents.models import Ivent, Team, RegionalPartner


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class RegionalPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalPartner
        fields = '__all__'


class IventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ivent
        fields = '__all__'



