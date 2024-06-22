from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from abc import ABC

from django.contrib.auth.models import AnonymousUser
from commons.middlewares.exception import *
from participant.models import *
from authentication.models.users import *

import random

TYPE = ['proporsional', 'district']

class ParticipantService(ABC):
    
    @classmethod
    @transaction.atomic
    def submit_user_data(cls, **data) :
        participant = Participant.objects.create(**data)

        auth_user = AuthUser.objects.create(participant=participant, name=participant.inisial)
        token = RefreshToken.for_user(auth_user)

        type = random.choice(TYPE)
        response_data = {
            'access_token': str(token.access_token),
            'type' : type
        }
        
        return response_data
    
    @classmethod
    def update_participant(cls, request, **data) :
        user = request.user
        if isinstance(user, AnonymousUser) :
            raise AuthenticationException("Authentication credentials were not provided or given token not valid.")
        participant = user.participant
        for key, value in data.items():
            setattr(participant, key, value)
        participant.save()
        return participant

