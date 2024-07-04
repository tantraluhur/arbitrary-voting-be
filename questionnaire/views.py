from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applibs.response import prepare_success_response, prepare_error_response, serializer_error_response
from commons.middlewares.exception import APIException

from record.serializers.simulation_serializer import *
from record.services import *

class QuestionnaireView(APIView):
    permission_classes = [IsAuthenticated, ]
    def __init__(self):
        super(QuestionnaireView, self).__init__()
        self.serializer = RecordSimulationSerializer
        self.submit_serializer = SubmitRecordSerializer
        self.service = RecordSimulationService
    
    def post(self, request) :
        try :
            serializer = self.submit_serializer(data=request.data)
            if(not serializer.is_valid()) :
                return Response(serializer_error_response(serializer.errors), status.HTTP_400_BAD_REQUEST)
            record = self.service.submit_record(request, **serializer.data)
            return Response(prepare_success_response("Record saved."), status.HTTP_201_CREATED)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)