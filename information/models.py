from django.db import models
from candidate.models import *


class Category(models.Model) :
    nama = models.CharField(max_length=120)

class Information(models.Model) :
    kategori = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    detail = models.TextField()


#for simulation
class CategorySimulation(models.Model) :
    nama = models.CharField(max_length=120)

class InformationSimulation(models.Model) :
    kategori = models.ForeignKey(CategorySimulation, on_delete=models.SET_NULL, null=True)
    choices = models.ForeignKey(ChoicesSimulation, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    deatil = models.TextField()