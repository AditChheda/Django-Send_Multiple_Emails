from django.db import models

# Create your models here.

class Upload_CSV(models.Model):
    uploaded_csv_file = models.FileField(upload_to='csv/')

    def __str__(self):
        return str(self.uploaded_csv_file)