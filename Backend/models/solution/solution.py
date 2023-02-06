from django.db import models
from Backend.models.problem.problem import Problem
from django.utils.timezone import now

class Solution(models.Model):
    show = models.BooleanField(default = True)
    user_id = models.IntegerField(default = 0)
    title = models.CharField(max_length = 64,default='题解')
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE,related_name="problem_solutions",null=True)
    create_time = models.DateTimeField(default = now)
    content = models.TextField(max_length=8*1024*1024, blank=True, default='')