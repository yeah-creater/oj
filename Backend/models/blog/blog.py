from django.db import models
from Backend.models.problem.problem import Problem
from Backend.models.file.file import File
from django.utils.timezone import now

class Blog(models.Model):
    show = models.BooleanField(default = True)
    file = models.OneToOneField(File,related_name='file_blog',on_delete=models.CASCADE,null=True) 
    user_id = models.IntegerField(default = 0)
    title = models.CharField(max_length = 64,default='题解',null=True)
    tags = models.CharField(max_length = 128,default='',null=True)
    create_time = models.DateTimeField(default = now)
    class Meta:
        ordering = ['-create_time']