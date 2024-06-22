from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applibs.response import prepare_success_response, prepare_error_response, serializer_error_response
from commons.middlewares.exception import APIException

from participant.services import *


from participant.serializer import *

class ParticipantView(APIView):
    
    def __init__(self):
        super(ParticipantView, self).__init__()
        self.serializer = ParticipantSerializer
        self.update_serializer = UpdateParticipantSerializer
        self.response_serializer = ResponseSerializer
        self.service = ParticipantService
    
    def post(self, request) :
        try :
            serializer = self.serializer(data=request.data)
            if(not serializer.is_valid()) :
                return Response(serializer_error_response(serializer.errors), status.HTTP_400_BAD_REQUEST)
            response = self.service.submit_user_data(**serializer.data)
            serializer_data = self.response_serializer(response).data
            return Response(prepare_success_response(serializer_data), status.HTTP_201_CREATED)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request) :
        try :
            serializer = self.update_serializer(data=request.data)
            if(not serializer.is_valid()) :
                return Response(serializer_error_response(serializer.errors), status.HTTP_400_BAD_REQUEST)
            participant = self.service.update_participant(request, **serializer.data)
            serializer_data = self.serializer(participant).data
            return Response(prepare_success_response(serializer_data), status.HTTP_200_OK)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)
        
