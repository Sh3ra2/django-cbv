from django.contrib import admin
from .models import employeemodel, projectmodel, clientmodel
# Register your models here.

admin.site.register(employeemodel)
admin.site.register(projectmodel)
admin.site.register(clientmodel)