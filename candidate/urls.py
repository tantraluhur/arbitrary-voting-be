from django.urls import path
from candidate.views import *


urlpatterns = [
    path('regional-political/', RegionPoliticalView.as_view()),
    path('national-political/', NationalPoliticalView.as_view()),
    path('', CandidateView.as_view())
]
