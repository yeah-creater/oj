from django.db import models

class SubmitRecord(models.Model):
    code = models.TextField(max_length=8*1024*1024, blank=True, default='')
    status = models.CharField(max_length=64, blank=True, default='')
    def __str__(self):
        return str(self.id)
class DebugRecord(models.Model):
    code = models.TextField(max_length=8*1024*1024, blank=True, default='')
    def __str__(self):
        return str(self.id)
