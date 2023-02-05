from django.db import models
import django.utils.timezone as timezone
class SubmitRecord(models.Model):
    user_id = models.IntegerField(blank=True,default = 0) 
    problem_id = models.IntegerField(blank=True,default = 0) 
    language = models.CharField(max_length=64, blank=True, default = 'C++')
    code = models.TextField(max_length=8*1024*1024, blank=True, default='')
    status = models.CharField(max_length=64, blank=True, default='')
    time = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.user_id)
    class Meta:
        ordering = ['-time']
class DebugRecord(models.Model):
    code = models.TextField(max_length=8*1024*1024, blank=True, default='')
    def __str__(self):
        return str(self.id)
