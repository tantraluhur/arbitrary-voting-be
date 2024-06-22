from django.db import models
from candidate.models import *


class Category(models.Model) :
    nama = models.CharField(max_length=120)

    def __str__(self) :
        return self.nama


class Information(models.Model) :
    kategori = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    kandidat = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    detail = models.TextField()

    def __str__(self) :
        return f"{self.kategori} - {self.kandidat.nama} ({self.kandidat.partai_politik.nama})"

#for simulation
class CategorySimulation(models.Model) :
    nama = models.CharField(max_length=120)

    def __str__(self) :
        return self.nama

class InformationSimulation(models.Model) :
    kategori = models.ForeignKey(CategorySimulation, on_delete=models.SET_NULL, null=True)
    kandidat = models.ForeignKey(CandidateSimulation, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    detail = models.TextField()

    def __str__(self) :
        return f"{self.kategori} - {self.kandidat.nama}"