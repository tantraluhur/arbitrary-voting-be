from django.urls import path
from information.views import *


urlpatterns = [
    path('', SimulationInformationView.as_view()),
]
