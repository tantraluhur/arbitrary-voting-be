from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applibs.response import prepare_success_response, prepare_error_response, serializer_error_response
from commons.middlewares.exception import APIException

from questionnaire.service import *
from questionnaire.serializer import *

class QuestionnaireView(APIView):
    permission_classes = [IsAuthenticated, ]
    def __init__(self):
        super(QuestionnaireView, self).__init__()
        self.serializer = QustionSerializer
        self.service = QustionService
    
    def get(self, request) :
        try :
            question = self.service.get_all_question()
            serializer_data = self.serializer(question, many=True).data
            return Response(prepare_success_response(serializer_data), status.HTTP_200_OK)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)