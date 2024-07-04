from django.db import transaction
from abc import ABC

from commons.middlewares.exception import *
from questionnaire.models import *

class QustionService(ABC):
    
    @classmethod
    @transaction.atomic
    def get_all_question(cls) :
        question = Quistionnaire.objects.all()
        return question
        

