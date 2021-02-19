from django.contrib import admin
from .models import Employee, Region

# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')
    
class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

admin.site.register(Region, RegionAdmin)
admin.site.register(Employee, EmployeeAdmin)

