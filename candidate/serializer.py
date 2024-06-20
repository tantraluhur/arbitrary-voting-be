from rest_framework import serializers
from candidate.models import *

class PoliticalPartySerializer(serializers.ModelSerializer) :
    class Meta:
        model = PoliticalParty
        fields = "__all__"