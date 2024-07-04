from django.urls import path
from information.views import *


urlpatterns = [
    path('', InformationView.as_view()),
    path('category/', CategoryView.as_view()),
    path('time-limit/', TimeLimitView.as_view()),
    path('auto-next/', AutoNextView.as_view()),

]
