from django.db import models
from Backend.models.problem.problem import Problem
from Backend.models.file.file import File
from django.utils.timezone import now

class Solution(models.Model):
    show = models.BooleanField(default = True)
    file = models.OneToOneField(File,related_name='file_solution',on_delete=models.CASCADE,null=True) 
    user_id = models.IntegerField(default = 0)
    title = models.CharField(max_length = 64,default='题解')
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE,related_name="problem_solutions",null=True)
    create_time = models.DateTimeField(default = now)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-create_time']