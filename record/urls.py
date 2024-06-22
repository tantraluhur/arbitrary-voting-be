from django.urls import path

from record.views import *


urlpatterns = [
    path('', RecordView.as_view()),
]