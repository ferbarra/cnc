from django.db import models

# Create your models here.

class StatusReport(models.Model):
    report_id = models.IntegerField()
    status = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
