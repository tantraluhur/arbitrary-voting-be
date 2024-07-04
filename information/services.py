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
        
        if(params == "district") :
            kategori_list = Category.objects.all()
            info_list = Information.objects.filter(kandidat__district=True).order_by('?')
            response = {
                "kategori" : kategori_list,
                "kandidat" : info_list
            }
            return response
        
    @classmethod
    def get_category(cls, request) :
        params = request.GET.get("type", '')
        
        params = params.lower()
        if(params == "simulation") :
            kategori_list = CategorySimulation.objects.all()
            return kategori_list
        
        else :
            kategori_list = Category.objects.all()
            return kategori_list
        
    @classmethod
    def get_time_limt(cls, request) :
        params = request.GET.get("type", '')
        
        params = params.lower()
        if(params == "simulation") :
            time_limit = TimeLimitSimulation.objects.first()
            if(not time_limit) :
                return {
                    "time" : 15
                }
            return time_limit
        
        else :
            time_limit = TimeLimit.objects.first()
            if(not time_limit) :
                return {
                    "time" : 15
                }
            return time_limit
        
    @classmethod
    def get_auto_next(cls, request) :
        params = request.GET.get("type", '')
        
        params = params.lower()
        if(params == "simulation") :
            auto_next = AutoNextSimulation.objects.first()
            if(not auto_next) :
                return {
                    "auto" : True
                }
            return auto_next
        
        else :
            auto_next = AutoNext.objects.first()
            if(not auto_next) :
                return {
                    "auto" : True
                }
            return auto_next
        

