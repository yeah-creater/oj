from django.db import models
from Backend.models.problem.problem import Problem
from Backend.models.file.file import File
from django.utils.timezone import now

class Video(models.Model):
    show = models.BooleanField(default = True)
    file = models.OneToOneField(File,related_name='file_video',on_delete=models.CASCADE,null=True) 
    user_id = models.IntegerField(default = 0)
    title = models.CharField(max_length = 64,default='视频题解')
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE,related_name="problem_videos",null=True)
    create_time = models.DateTimeField(default = now)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-create_time']