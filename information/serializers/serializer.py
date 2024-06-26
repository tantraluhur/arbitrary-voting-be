from rest_framework import serializers
from information.models import *
from candidate.models import *

class CandidateSimulationSerializer(serializers.ModelSerializer) :
    class Meta:
        model = CandidateSimulation
        fields = "__all__"

class CategorySimulationSerializer(serializers.ModelSerializer) :
    class Meta:
        model = CategorySimulation
        fields = "__all__"

class InformationSimulationSerializer(serializers.ModelSerializer) :
    kategori = serializers.CharField(source="kategori.nama")
    nama = serializers.CharField(source="kandidat.nama")
    partai = serializers.SerializerMethodField()

    class Meta:
        model = Information
        fields = "__all__"

    def get_partai(self, obj):
        if hasattr(obj.kandidat, 'partai_politik') :
            return obj.kandidat.partai_politik.nama if obj.kandidat.partai_politik else None
        return None
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('partai') is None:
            representation.pop('partai')
        return representation

class ResponseSerializer(serializers.Serializer) :
    kategori = CategorySimulationSerializer(many=True)
    kandidat = InformationSimulationSerializer(many=True)

class CategorySerializer(serializers.ModelSerializer) :

    class Meta :
        model = CategorySimulation
        fields = "__all__" 
