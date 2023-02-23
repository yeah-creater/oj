from django.db import models
from django.contrib.auth.models import User
import os
from simplepro.editor import fields
from django.utils.html import format_html
DIFFICULTY_CHOICES=(('简单','简单'),
              ('中等','中等'),
              ('困难','困难'),)

TIME_LIMIT_CHOICES=((1,1),(2,2),(5,5))
SPACE_LIMIT_CHOICES=((64,64),(128,128),(512,512))
SOURCE_CHOICES=(('ZCOJ','ZCOJ'),
                ('Acwing','AcWing'),
                ('洛谷','洛谷'),
                ('Codeforces','Codeforces'))


class Problem(models.Model):
    show = models.BooleanField(default = False, blank=True)
    title = models.CharField(max_length=100, blank=True, default='')
    tags = models.CharField(max_length=100, blank=True, default='')
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, default='简单', max_length=20)
    time_limit = models.IntegerField(choices = TIME_LIMIT_CHOICES, default = 1)
    space_limit = models.IntegerField(choices = SPACE_LIMIT_CHOICES, default = 64)
    submit_nums = models.IntegerField(default=0)
    ac_nums = models.IntegerField(default=0)
    source = models.CharField(choices=SOURCE_CHOICES, default='ZCOJ', max_length=30)
    description = fields.MDTextField(max_length=256*1024,blank=True,default='')
    input_format = fields.MDTextField(max_length=128*1024,blank=True,default='')
    output_format = fields.MDTextField(max_length=128*1024,blank=True,default='')
    data_range = fields.MDTextField(max_length=32*1024,blank=True,default='')
    input_example = fields.MDTextField(max_length=32*1024,blank=True,default='')
    output_example = fields.MDTextField(max_length=32*1024,blank=True,default='')
    contest = models.IntegerField(default = 0)
    def __str__(self):
        return self.title
    def Difficulty(self):
        if self.difficulty == '简单':
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">简单</span>')
        elif self.difficulty == '中等':
            format_td = format_html('<span style="padding:2px;background-color:gold;color:gray">中等</span>')
        else:
            format_td = format_html('<span style="padding:2px;background-color:red;color:black">困难</span>')
        return format_td
    Difficulty.short_description = "difficulty"
    class Meta:
        ordering = ['id']

class AcProblem(models.Model):
    problem = models.ForeignKey(Problem,related_name='problem_ac',on_delete=models.CASCADE,null=True) 
    user = models.ForeignKey(User,related_name='user_ac',on_delete=models.CASCADE,null=True) 

    def __str__(self):
        return str(self.user.id)+'->'+str(self.problem.id)