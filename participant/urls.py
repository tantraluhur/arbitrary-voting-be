from django.urls import path
from participant.views import *


urlpatterns = [

    path('', ParticipantView.as_view()),

]
