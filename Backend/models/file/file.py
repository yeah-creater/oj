from django.db import models

class File(models.Model):
    content = models.TextField(max_length=8*1024*1024, blank=True, default='')
    