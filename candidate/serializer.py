from rest_framework import serializers
from candidate.models import *

class PoliticalPartySerializer(serializers.ModelSerializer) :
    class Meta:
        model = PoliticalParty
        fields = "__all__"


class CandidateSerializer(serializers.Serializer) :
    nama = serializers.CharField()

class ResponseSerializer(serializers.Serializer) :
    partai = serializers.CharField()
    kandidat = CandidateSerializer(many=True)