from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applibs.response import prepare_success_response, prepare_error_response, serializer_error_response
from commons.middlewares.exception import APIException

from candidate.models import *
from candidate.serializer import *
from candidate.services import *

class CandidateView(APIView):
    permission_classes = [IsAuthenticated, ]
    
    def __init__(self):
        super(CandidateView, self).__init__()
        self.serializer = ResponseSerializer
        self.service = CandidateService
    
    def get(self, request) :
        try :
            response = self.service.get_all_kandidat(request)
            return Response(prepare_success_response(response), status.HTTP_200_OK)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegionPoliticalView(APIView) :
    permission_classes = [IsAuthenticated, ]

    def __init__(self):
        super(RegionPoliticalView, self).__init__()
        self.serializer = PoliticalPartySerializer

    def get(self, request) :
        political_list = RegionPoliticalParty.objects.all()
        serializer_data = self.serializer(political_list, many=True).data
        return Response(prepare_success_response(serializer_data), status.HTTP_200_OK)

class NationalPoliticalView(APIView) :
    permission_classes = [IsAuthenticated, ]

    def __init__(self):
        super(NationalPoliticalView, self).__init__()
        self.serializer = PoliticalPartySerializer

    def get(self, request) :
        political_list = NationalPoliticalParty.objects.all()
        serializer_data = self.serializer(political_list, many=True).data
        return Response(prepare_success_response(serializer_data), status.HTTP_200_OK)



