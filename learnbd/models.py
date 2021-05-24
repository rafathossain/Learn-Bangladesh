from django.db import models


# Create your models here.
class DistrictSummary(models.Model):
    dist_id = models.CharField(max_length=200)
    dist_summary = models.TextField()
