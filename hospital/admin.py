from django.contrib import admin
from .models import *   #importing all the models
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
