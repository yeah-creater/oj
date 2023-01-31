from django.urls import path,include
from Backend.views.problem.content import ContentView
from Backend.views.problem.list import ListView
from Backend.views.problem.judge import JudgeView

urlpatterns = [
    path('content/', ContentView.as_view(), name='problem_content'),
    path('list/', ListView.as_view(), name='problem_list'),
    path('judge/', JudgeView.as_view(), name='problem_judge'),
]