from django.contrib import admin
from candidate.models import *

class CustomCandidateAdmin(admin.ModelAdmin):
    model = Candidate
    list_filter = ('partai_politik', )

admin.site.register(CandidateSimulation)
admin.site.register(NationalPoliticalParty)
admin.site.register(RegionPoliticalParty)
admin.site.register(PoliticalParty)
admin.site.register(Candidate, CustomCandidateAdmin)