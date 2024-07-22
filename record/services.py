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
        
    @classmethod
    def submit_duration_category(cls, request, **data) :
        kategori = data.get("kategori")
        duration = data.get("durasi")
        participant = request.user.participant
        duration_object = DurationCategoryRecord.objects.filter(kategori=kategori, participant=participant).first()

        if(not duration_object) :
            duration_object = DurationCategoryRecord.objects.create(kategori=kategori, duration=duration, participant=participant, inisial=participant.inisial)
            return
        duration += duration_object.duration
        duration_object.duration = duration
        duration_object.save()
