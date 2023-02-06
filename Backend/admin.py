from django.contrib import admin
from Backend.models.problem.problem import Problem
from Backend.models.judge_record.judge_record import SubmitRecord
from Backend.models.judge_record.judge_record import DebugRecord
from Backend.models.user.user import UserInfo
from Backend.models.user.user import Follow
from Backend.models.solution.solution import Solution
# Register your models here.
admin.site.register(Problem)

admin.site.register(SubmitRecord)
admin.site.register(DebugRecord)
admin.site.register(UserInfo)
admin.site.register(Follow)

admin.site.register(Solution)