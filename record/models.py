from django.db import models

from participant.models import *

class RecordProporsional(models.Model) :
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inisial = models.CharField(max_length=120)
    kandidat = models.CharField(max_length=120)
    partai = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)
    durasi = models.IntegerField(null=True, blank=True)

class RecordDistrict(models.Model) :
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inisial = models.CharField(max_length=120)
    kandidat = models.CharField(max_length=120)
    partai = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)
    durasi = models.IntegerField(null=True, blank=True)

class DurationCategoryRecord(models.Model) :
    kategori = models.CharField(max_length=120)
    duration = models.IntegerField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, blank=True)
    inisial = models.CharField(max_length=120, null=True, blank=True)

#for simulation
class RecordSimulation(models.Model) :
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inisial = models.CharField(max_length=120)
    kandidat = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)
    durasi = models.IntegerField(null=True, blank=True)
