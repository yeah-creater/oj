from django.urls import path,include
from Backend.views.solution.list import ListView
from Backend.views.solution.content import ContentView
from Backend.views.solution.operation import OperationView
from Backend.views.solution.search import SearchView
urlpatterns = [
    path('list/', ListView.as_view(), name='solution_list'),
    path('content/', ContentView.as_view(), name='solution_content'),
    path('operation/',OperationView.as_view(), name='solution_operation'),
    path('search/', SearchView.as_view(), name='solution_search'),
]