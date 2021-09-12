from django.contrib import admin
from . models import Upload_CSV
# Register your models here.

@admin.register(Upload_CSV)
class Upload_CSV_ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'uploaded_csv_file']