from django.db import transaction
from abc import ABC

from commons.middlewares.exception import BadRequestException
from record.models import *

class RecordSimulationService(ABC):
    
    @classmethod
    def submit_record(cls,request, **data) :
        params = request.GET.get("type", None)
        user = request.user
        participant = user.participant
        data['participant'] = participant
        data['inisial'] = participant.inisial

        if not params :
            raise BadRequestException("Query Params cannot be None.")
        
        params = params.lower()

        if(params == "simulation") :
            if(data.get("partai")) :
                raise BadRequestException("Please use valid query params.")
            record = RecordSimulation.objects.create(**data)
            return record
        
        if(params == "proporsional") :
            record = RecordProporsional.objects.create(**data)
            return record
        
        if(params == "district") :
            record = RecordDistrict.objects.create(**data)
            return record