from django.db import models
import django.utils.timezone as timezone
from django.utils.html import format_html

class SubmitRecord(models.Model):
    user_id = models.IntegerField(blank=True,default = 0) 
    problem_id = models.IntegerField(blank=True,default = 0) 
    language = models.CharField(max_length=64, blank=True, default = 'C++')
    code = models.TextField(max_length=8*1024*1024, blank=True, default='')
    status = models.CharField(max_length=64, blank=True, default='')
    time = models.DateTimeField(default = timezone.now)
    contest_id = models.IntegerField(blank=True,default = 0)
    def __str__(self):
        return str(self.user_id)
    def Status(self):
        if self.status == 'Accepted':
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">'+self.status+'</span>')
        else:
            format_td = format_html('<span style="padding:2px;background-color:red;color:black">'+self.status+'</span>')
        return format_td
    class Meta:
        ordering = ['-time']
class DebugRecord(models.Model):
    code = models.TextField(max_length=8*1024*1024, blank=True, default='')
    def __str__(self):
        return str(self.id)
