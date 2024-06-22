import enum
from django.db import models

from candidate.models import *

class Participant(models.Model) :
    class JenisKelamin(str, enum.Enum):
        L = "L"
        P = "P"

        @classmethod
        def choices(cls):
            return [(item.value, item.name) for item in cls]
    
    inisial = models.CharField(max_length=1)
    jenis_kelamin = models.CharField(max_length=1, choices=JenisKelamin.choices())
    usia = models.IntegerField()
    partai_nasional = models.CharField(max_length=120)
    partai_daerah = models.CharField(max_length=120)
    bersedia = models.BooleanField(default=True)

    #simulation attr
    start_date_simulation = models.DateTimeField(null=True, blank=True)
    end_date_simulation = models.DateTimeField(null=True, blank=True)
    information_check_simulation = models.TextField(null=True, blank=True)
    final_answer_simulation = models.CharField(max_length=120, null=True, blank=True)

    information_check = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    final_answer = models.CharField(max_length=120, null=True, blank=True)

