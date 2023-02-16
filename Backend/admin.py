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
# Register your models here.
admin.site.register(Problem)
admin.site.register(AcProblem)

admin.site.register(SubmitRecord)
admin.site.register(DebugRecord)
admin.site.register(UserInfo)
admin.site.register(Follow)

admin.site.register(Solution)
admin.site.register(Blog)
admin.site.register(Video)


admin.site.register(File)
admin.site.register(Comment)
admin.site.register(FileLike)
admin.site.register(CommentLike)

admin.site.register(ChatList)
admin.site.register(ChatMessage)

admin.site.register(Log)

admin.site.register(Contest)
admin.site.register(ContestParticipant)



