from django.urls import path,include
from Backend.views.blog.list import ListView
from Backend.views.blog.content import ContentView
from Backend.views.blog.operation import OperationView
from Backend.views.blog.search import SearchView
urlpatterns = [
    path('list/', ListView.as_view(), name='blog_list'),
    path('content/', ContentView.as_view(), name='blog_content'),
    path('operation/',OperationView.as_view(), name='blog_operation'),
    path('search/', SearchView.as_view(), name='blog_search'),
]