from django.urls import path
from questionnaire.views import *

urlpatterns = [
    path('', QuestionnaireView.as_view()),
]
