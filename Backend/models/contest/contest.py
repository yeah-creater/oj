from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from Backend.models.file.file import File
class Contest(models.Model):
    name = models.CharField(max_length=128,default='第x次周赛')
    user = models.ForeignKey(User,related_name='user_contest',on_delete=models.CASCADE,null=True) 
    participants = models.IntegerField(default = 0)
    file = models.OneToOneField(File,related_name='file_contest',on_delete=models.CASCADE,null=True) 

    start_time = models.DateTimeField(default = now)
    over_time = models.DateTimeField(default = now)
    class Meta:
        ordering = ['-start_time']

class ContestParticipant(models.Model):
    contest = models.ForeignKey(Contest,related_name='contest_participant',on_delete=models.CASCADE,null=True) 
    user = models.ForeignKey(User,related_name='user_participatant',on_delete=models.CASCADE,null=True) 
    score = models.IntegerField(default = 0)
    penalty =models.IntegerField(default = 0) # 单位为秒 
    register_time = models.DateTimeField(default = now)
    def __str__(self):
        return str(self.user.id)+'->'+str(self.contest.id)
    class Meta:
        ordering = ['-score','penalty']

