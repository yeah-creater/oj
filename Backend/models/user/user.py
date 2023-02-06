from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
GENDER_CHOICES=(('male','男'),
              ('female','女'))
class UserInfo(models.Model):
    forbidden = models.BooleanField(default = False, blank=True)
    user = models.OneToOneField(User,related_name='user_info',on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=64,default='Trainee')
    gender = models.CharField(choices = GENDER_CHOICES,default='male',max_length=16)
    birthday = models.DateField(default = now)
    photo = models.URLField(max_length=256,blank=True,default="https://app2105.acapp.acwing.com.cn/media/profile/default.jpg")
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
