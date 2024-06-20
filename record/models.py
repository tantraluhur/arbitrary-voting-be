from django.db import models

class Record(models.Model) :
    inisial = models.CharField(max_length=120)
    kandidat = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)


#for simulation
class RecordSimulation(models.Model) :
    insial = models.CharField(max_length=120)
    choices = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)
