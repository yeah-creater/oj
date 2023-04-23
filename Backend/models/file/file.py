from django.db import models
from django.utils.timezone import now

class File(models.Model):
    content = models.TextField(max_length=8*1024*1024, blank=True, default='')
    def __str__(self):
        return str(self.id)
# 2->3 表示 2用户点赞 3文件
class FileLike(models.Model):
    source = models.IntegerField(default = 0)
    target = models.IntegerField(default = 0)
    time = models.DateTimeField(default = now)
    def __str__(self):
        return str(self.source) + ' good at ' + str(self.target)

# 字段名称不得已与前端接口一致
class Comment(models.Model):
    file = models.ForeignKey(File,related_name='file_comments',on_delete=models.CASCADE,null = True)
    uid = models.IntegerField(default = 0)
    parentId = models.IntegerField(default = 0)
    content = models.TextField(max_length=8*1024*1024, blank=True, default='')
    likes = models.IntegerField(default = 0)
    address = models.CharField(max_length = 1024,default = '中国')
    createTime = models.DateTimeField(default = now)
    class Meta:
        ordering = ['-createTime']
    def __str__(self):
        return str(self.uid)+':'+self.content
    
# 2->3 表示 2用户点赞 3评论
class CommentLike(models.Model):
    source = models.IntegerField(default=0)
    target = models.IntegerField(default=0)
    time = models.DateTimeField(default = now)
    def __str__(self):
        return str(self.source) + ' - ' + str(self.target)