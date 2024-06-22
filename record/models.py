from django.db import models

from participant.models import *

class RecordProporsional(models.Model) :
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inisial = models.CharField(max_length=120)
    kandidat = models.CharField(max_length=120)
    partai = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)

class RecordDistrict(models.Model) :
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inisial = models.CharField(max_length=120)
    kandidat = models.CharField(max_length=120)
    partai = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)

#for simulation
class RecordSimulation(models.Model) :
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inisial = models.CharField(max_length=120)
    kandidat = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)
