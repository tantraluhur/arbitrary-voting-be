from rest_framework import serializers

from questionnaire.models import *

class QustionSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Quistionnaire
        fields = "__all__"
