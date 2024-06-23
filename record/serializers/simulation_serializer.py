from rest_framework import serializers

from record.models import *

class RecordSimulationSerializer(serializers.ModelSerializer) :
    class Meta :
        model = RecordSimulation
        fields = "__all__"

class SubmitRecordSerializer(serializers.Serializer) :
    kandidat = serializers.CharField()
    kategori = serializers.CharField()
    partai = serializers.CharField(required=False)
    durasi = serializers.IntegerField()

