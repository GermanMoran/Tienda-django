from django.contrib import admin
from .models import servicios
# Register your models here.


# Esta clase es para mostrar los servicios de solo lectura
class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(servicios,servicioAdmin)