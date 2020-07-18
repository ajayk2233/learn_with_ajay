from django.contrib import admin
from .models import Blog
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ImportExportAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Blog,ImportExportModelAdmin)