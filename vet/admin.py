from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Usuario)
admin.site.register(models.Clinica)
admin.site.register(models.Mascota)
admin.site.register(models.Diagnostico)
admin.site.register(models.Trabaja)