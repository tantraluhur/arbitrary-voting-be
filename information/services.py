from django.db import transaction
from abc import ABC

from commons.middlewares.exception import *
from information.models import *

class InformationService(ABC):
    
    @classmethod
    @transaction.atomic
    def get_all_info(cls, request) :
        params = request.GET.get("type", None)

        if not params :
            raise BadRequestException("Query Params cannot be None.")
        
        params = params.lower()

        if(params == "simulation") :
            kategori_list = CategorySimulation.objects.all()
            info_list = InformationSimulation.objects.all().order_by('?')
            response = {
                "kategori" : kategori_list,
                "kandidat" : info_list
            }
            return response
        
        if(params == "proporsional") :
            kategori_list = Category.objects.all()
            info_list = Information.objects.all().order_by('?')
            response = {
                "kategori" : kategori_list,
                "kandidat" : info_list
            }
            return response 
        
        if(params == "disctrict") :
            kategori_list = Category.objects.all()
            info_list = Information.objects.filter(kandidat__district=True).order_by('?')
            response = {
                "kategori" : kategori_list,
                "kandidat" : info_list
            }
            return response 


