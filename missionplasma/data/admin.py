from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class StudentResource(resources.ModelResource):
   class Meta:
      model = State
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource
   
admin.site.register(City)
admin.site.register(State,StudentAdmin)
admin.site.register(Donor)
admin.site.register(Requester)