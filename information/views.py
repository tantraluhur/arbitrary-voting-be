from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applibs.response import prepare_success_response, prepare_error_response, serializer_error_response
from commons.middlewares.exception import APIException

from information.serializers.serializer import *
from information.services import *

class SimulationInformationView(APIView):
    permission_classes = [IsAuthenticated, ]

    def __init__(self) :
        self.serializer = ResponseSerializer
        self.service = InformationService

    def get(self, request) :
        try :
            response = self.service.get_all_info(request)
            serializer_data = self.serializer(response).data
            return Response(prepare_success_response(serializer_data), status.HTTP_200_OK)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CategoryView(APIView) :
    permission_classes = [IsAuthenticated]

    def __init__(self) :
        self.serializer = CategorySerializer
        self.service = InformationService
    
    def get(self, request) :
        try :
            kategori = self.service.get_category(request)
            serializer_data = self.serializer(kategori).data
            return Response(prepare_success_response(serializer_data), status.HTTP_200_OK)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)



