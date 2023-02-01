from django.contrib import admin
from Backend.models.snippets.snippet import Snippet
from Backend.models.problem.problem import Problem
from Backend.models.problem.problem import ProblemLimit
from Backend.models.problem.problem import ProblemSource
from Backend.models.judge_record.judge_record import SubmitRecord
from Backend.models.judge_record.judge_record import DebugRecord

# Register your models here.
admin.site.register(Snippet)
admin.site.register(Problem)
admin.site.register(ProblemLimit)
admin.site.register(ProblemSource)
admin.site.register(SubmitRecord)
admin.site.register(DebugRecord)