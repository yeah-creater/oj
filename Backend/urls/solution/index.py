from django.urls import path,include
from Backend.views.solution.list import ListView


urlpatterns = [
    path('list/', ListView.as_view(), name='solution_list'),
]