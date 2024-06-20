from rest_framework import serializers
from participant.models import Participant

class ParticipantSerializer(serializers.ModelSerializer) :
    start_date = serializers.DateTimeField()
    class Meta:
        model = Participant
        fields = "__all__"


class TokenSerializer(serializers.Serializer) :
    access_token = serializers.CharField()

