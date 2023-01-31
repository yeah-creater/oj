from django.db import models


DIFFICULTY_CHOICES=(('简单','简单'),
              ('中等','中等'),
              ('困难','困难'),)
LIMIT_CHOICES=(('1s/64M','1s/64M'),
              ('2s/128M','2s/128M'),
              ('5s/512M','5s/512M'),)
SOURCE_CHOICES=(('ZCOJ','ZCOJ'),
                ('Acwing','AcWing'),
                ('洛谷','洛谷'),
                ('Codeforces','Codeforces'))
class Problem(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    tags = models.CharField(max_length=100, blank=True, default='')
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, default='简单', max_length=20)
    limit = models.CharField(choices=LIMIT_CHOICES, default='1s/64M', max_length=20)
    source = models.CharField(choices=SOURCE_CHOICES, default='ZCOJ', max_length=30)
    description = models.TextField(max_length=128*1024,blank=True,default='')
    input_format = models.TextField(max_length=32*1024,blank=True,default='')
    output_format = models.TextField(max_length=32*1024,blank=True,default='')
    data_range = models.TextField(max_length=32*1024,blank=True,default='')
    input_example = models.TextField(max_length=32*1024,blank=True,default='')
    output_example = models.TextField(max_length=32*1024,blank=True,default='')
    
    def __str__(self):
        return self.title
