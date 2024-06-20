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

class ParticipantSession(models.Model) :
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    durasi = models.IntegerField(null=True, blank=True)

#for simulation
class ParticipantSimulationSession(models.Model) :
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    durasi = models.IntegerField(null=True, blank=True)