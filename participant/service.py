from django.db.models import Q
from django.db import transaction
from abc import ABC

from participant.models import Participant

class UserPersonilService(ABC):
    
    @classmethod
    @transaction.atomic
    def submit_data(cls, **data) :
        participant = Participant.objects.create(**data)
        return participant

