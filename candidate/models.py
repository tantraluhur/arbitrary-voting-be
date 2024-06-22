from django.db import models

class NationalPoliticalParty(models.Model) :
    nama = models.CharField(max_length=120)

    def __str__(self) :
        return self.nama

class RegionPoliticalParty(models.Model) :
    nama = models.CharField(max_length=120)

    def __str__(self) :
        return self.nama

class PoliticalParty(models.Model) :
    nama = models.CharField(max_length=120)

    def __str__(self) :
        return self.nama

class Candidate(models.Model) :
    nama = models.CharField(max_length=120)
    partai_politik = models.ForeignKey(PoliticalParty, on_delete=models.SET_NULL, null=True)
    district = models.BooleanField(default=False)
    def __str__(self) :
        if(self.partai_politik) :
            return f"{self.nama} - {self.partai_politik.nama}"
        else :
            return self.nama
        
#for simulation
class CandidateSimulation(models.Model) :
    nama = models.CharField(max_length=120)

    def __str__(self) :
        return self.nama

