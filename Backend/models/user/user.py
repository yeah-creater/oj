from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    forbidden = models.BooleanField(default = False, blank=True)
    user = models.OneToOneField(User,related_name='user_info',on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=64,default='Trainee')
    photo = models.URLField(max_length=256,blank=True,default="http://106.15.183.53:8000/media/profile/default.jpg")
    followings = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)

# Follow图 7-8 表示7关注8
class Follow(models.Model):
    source = models.IntegerField(default=0)
    target = models.IntegerField(default=0)
    def __str__(self):
        return str(self.source) + ' - ' + str(self.target)
