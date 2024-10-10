from django.db import models

class DataFrameModel(models.Model):
    column_1 = models.CharField(max_length=255)  # Change CharField to the appropriate field type based on your data
    column_2 = models.CharField(max_length=255)
    column_3 = models.CharField(max_length=255)
    column_4 = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
