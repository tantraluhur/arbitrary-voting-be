from django.db import models

class NationalPoliticalParty(models.Model) :
    nama = models.CharField(max_length=120)

class RegionPoliticalParty(models.Model) :
    nama = models.CharField(max_length=120)

class PoliticalParty(models.Model) :
    nama = models.CharField(max_length=120)

class Candidate(models.Model) :
    nama = models.CharField(max_length=120)
    partai_politik = models.ForeignKey(PoliticalParty, on_delete=models.SET_NULL, null=True)

#for simulation
class ChoicesSimulation(models.Model) :
    nama = models.CharField(max_length=120)

