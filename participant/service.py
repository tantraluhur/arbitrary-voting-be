from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from abc import ABC

from participant.models import *

class ParticipantService(ABC):
    
    @classmethod
    @transaction.atomic
    def submit_user_data(cls, **data) :
        start_date = data.pop("start_date")
        participant = Participant.objects.create(**data)
        ParticipantSession.objects.create(start_date=start_date)
        token = RefreshToken.for_user(participant)

        response_data = {
            'access_token': str(token.access_token),
        }
        
        return response_data

