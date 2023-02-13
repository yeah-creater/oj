from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
class ChatList(models.Model):
    source = models.ForeignKey(User,related_name='user_send_list',on_delete=models.CASCADE,null=True)
    target = models.ForeignKey(User,related_name='user_receive_list',on_delete=models.CASCADE,null=True)
    unread = models.IntegerField(default = 0)
    update_time = models.DateTimeField(default = now)
    def __str__(self):
        return str(self.source)
    class Meta:
        ordering = ['-update_time']

class ChatMessage(models.Model):
    source = models.ForeignKey(User,related_name='user_send_message',on_delete=models.CASCADE,null=True)
    target = models.ForeignKey(User,related_name='user_receive_message',on_delete=models.CASCADE,null=True)
    content = models.TextField(max_length=2048,null=True)
    create_time = models.DateTimeField(default = now)
    class Meta:
        ordering = ['create_time']