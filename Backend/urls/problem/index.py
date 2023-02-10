from django.urls import path,include
from Backend.views.problem.content import ContentView
from Backend.views.problem.list import ListView
from Backend.views.problem.title import TitleView
from Backend.views.problem.search import SearchView
from Backend.views.problem.judge import JudgeView
from Backend.views.problem.upload_test_case import UploadTestCaseView

urlpatterns = [
    path('content/', ContentView.as_view(), name='problem_content'),
    path('list/', ListView.as_view(), name='problem_list'),
    path('title/', TitleView.as_view(), name='problem_title'),
    path('search/', SearchView.as_view(), name='problem_search'),
    path('judge/', JudgeView.as_view(), name='problem_judge'),
    path('upload_test_case/', UploadTestCaseView.as_view(), name='problem_upload_test_case'),
]