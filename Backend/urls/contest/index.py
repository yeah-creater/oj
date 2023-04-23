from django.urls import path,include
from Backend.views.contest.list import ListView
from Backend.views.contest.participant import ParticipantView
from Backend.views.contest.problem import ProblemListView
from Backend.views.contest.standing import StandingView
from Backend.views.contest.content import ContentView
from Backend.views.contest.rating import RatingView
urlpatterns = [
    path('list/', ListView.as_view(), name='content_list'),
    path('participant/', ParticipantView.as_view(), name='contest_participant'),
    path('problem/', ProblemListView.as_view(), name='contest_problem_list'),
    path('standing/', StandingView.as_view(), name='contest_standing'),
    path('content/', ContentView.as_view(), name='contest_content'),
    path('rating/', RatingView.as_view(), name='contest_rating'),
]