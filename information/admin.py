from django.contrib import admin
from information.models import *
# Register your models here.


admin.site.register(InformationSimulation)
admin.site.register(CategorySimulation)

admin.site.register(Category)
admin.site.register(Information)

admin.site.register(TimeLimit)
admin.site.register(TimeLimitSimulation)

admin.site.register(AutoNext)
admin.site.register(AutoNextSimulation)
