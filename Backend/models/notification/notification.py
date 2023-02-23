from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
TYPE_CHOICES=(('关注了','关注了'),
              ('评论了','评论了'))
class Notification(models.Model):
    source = models.ForeignKey(User,related_name='user_receive_notification',on_delete=models.CASCADE,null=True)
    target = models.ForeignKey(User,related_name='user_send_notification',on_delete=models.CASCADE,null=True)
    notification_type = models.CharField(choices = TYPE_CHOICES,default = '关注了我',max_length = 32)
    read = models.BooleanField(default = False)
    time = models.DateTimeField(default = now)
    def __str__(self):
        return str(self.target.id)+self.notification_type+str(self.source.id)
    class Meta:
        ordering = ['-time']

