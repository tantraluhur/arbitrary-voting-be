from django.db import transaction
from abc import ABC

from commons.middlewares.exception import *
from information.models import *

class CandidateService(ABC):
    
    @classmethod
    @transaction.atomic
    def get_all_kandidat(cls, request) :
        params = request.GET.get("type", None)

        if not params :
            raise BadRequestException("Query Params cannot be None.")
        
        params = params.lower()

        if(params == "simulation") :
            response = []
            info_list = CandidateSimulation.objects.all().order_by('?')
            for i in info_list :
                response.append({
                    "partai" : None,
                    "kandidat" : [{
                        "nama" : i.nama
                    }]
                })
            return response
        
        if(params == "proporsional") :
            temp = {}
            kandidat_list = Candidate.objects.all().order_by("?")
            for i in kandidat_list :
                partai = temp.get(i.partai_politik.nama, None)
                if(not partai) :
                    temp[i.partai_politik.nama] = []

                data = {
                    "nama" : i.nama
                }
                temp[i.partai_politik.nama].append(data)
            response = []
            for key, value in temp.items() :
                response.append({
                    "partai" : key,
                    "kandidat" : value
                })
            return response
        
        if(params == "district") :
            response = []
            info_list = Candidate.objects.filter(district=True).order_by('?')
            for i in info_list :
                response.append({
                    "partai" : i.partai_politik.nama,
                    "kandidat" : [{
                        "nama" : i.nama
                    }]
                })

            return response