from rest_framework import serializers
from participant.models import Participant

class ParticipantSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Participant
        fields = "__all__"

class ResponseSerializer(serializers.Serializer) :
    access_token = serializers.CharField()
    type = serializers.CharField()

class UpdateParticipantSerializer(serializers.Serializer) :
    information_check = serializers.CharField(required=False)
    information_check_simulation = serializers.CharField(required=False)

    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)

    start_date_simulation = serializers.DateTimeField(required=False)
    end_date_simulation = serializers.DateTimeField(required=False)

    final_answer_simulation = serializers.CharField(required=False)
    final_answer = serializers.CharField(required=False)

    participant_question_answer = serializers.ListField(required=False)

    prioritas_kategori = serializers.JSONField(required=False)

