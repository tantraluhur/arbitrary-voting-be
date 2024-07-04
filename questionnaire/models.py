import enum
from django.db import models

class Quistionnaire(models.Model) :
    class Type(str, enum.Enum):
        LIKERT = "likert"
        TEXT = "text"

        @classmethod
        def choices(cls):
            return [(item.value, item.name) for item in cls]
        
    question = models.CharField(max_length=255)
    type = models.CharField(max_length=12, choices=Type.choices())
    scale = models.IntegerField(null=True, blank=True)

