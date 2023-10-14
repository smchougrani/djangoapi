from django.contrib import admin

from appoitment.models import Appointment, DemandeSoin, Medecin

# Register your models here.



admin.site.register(Appointment)
admin.site.register(DemandeSoin)
admin.site.register(Medecin)

