from django.contrib import admin
from Backend.models.problem.problem import Problem
from Backend.models.problem.problem import AcProblem
from Backend.models.judge_record.judge_record import SubmitRecord
from Backend.models.judge_record.judge_record import DebugRecord
from Backend.models.user.user import UserInfo
from Backend.models.user.user import Follow
from Backend.models.solution.solution import Solution
from Backend.models.blog.blog import Blog
from Backend.models.video.video import Video

from Backend.models.file.file import File
from Backend.models.file.file import FileLike
from Backend.models.file.file import Comment
from Backend.models.file.file import CommentLike

from Backend.models.chat.chat import ChatList
from Backend.models.chat.chat import ChatMessage

from Backend.models.log.log import Log

from Backend.models.contest.contest import Contest
from Backend.models.contest.contest import ContestParticipant

from Backend.models.notification.notification import Notification

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
admin.site.site_title="OnlineJudge后台"
admin.site.site_header = "OnlineJudge后台管理"
# Register your models here.
# admin.site.register(UserInfo)
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # list_display = 你需要展示的字段应该写在这里,此处是数据库中的字段
    list_display = ('user','name','sno','gender','address','Status')
    # search_fields = 用于添加一个搜索框
    search_fields = ('name','sno')
    # list_filter = 设置一个过滤器
    list_filter = ("name",'forbidden')
    # list_editable = ('name',)
    # readonly_fields = ("hostCPU","hostMEM",)
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    # list_display = 你需要展示的字段应该写在这里,此处是数据库中的字段
    list_display = ('title','source','Difficulty')
    # search_fields = 用于添加一个搜索框
    search_fields = ('title','source')
    # list_filter = 设置一个过滤器
    list_filter = ("title",'source')
@admin.register(AcProblem)
class AcProblemAdmin(admin.ModelAdmin):
    list_display = ('user','problem')
@admin.register(SubmitRecord)
class SubmitRecordAdmin(admin.ModelAdmin):
    list_display = ('user_id','problem_id','Status')
    # search_fields = 用于添加一个搜索框
    search_fields = ('user_id','problem_id','status')
    list_filter = ('user_id','problem_id','status')
admin.site.register(DebugRecord)

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('source','target')
    search_fields = ('source','target')
    list_filter = ('source','target')


@admin.register(Solution,Blog,Video)
class FileAdmin(admin.ModelAdmin):
    list_display = ('user_id','title','file')
    list_filter =  ('user_id','title','file')

admin.site.register(File)
admin.site.register(Comment)
admin.site.register(FileLike)
admin.site.register(CommentLike)

admin.site.register(ChatList)
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('source','target','content')
    list_filter =  ('source','target')

admin.site.register(Log)

admin.site.register(Contest)

class ProxyResource(resources.ModelResource):
    class Meta:
        model = ContestParticipant
@admin.register(ContestParticipant)
class ContestParticipantAdmin(ImportExportActionModelAdmin):
    list_display = ('contest','user','score','penalty')
    list_filter =  ('contest','user','score')
    resource_class = ProxyResource

admin.site.register(Notification)



