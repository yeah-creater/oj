from django.urls import path,include
from Backend.views.file.comment import CommentView
from Backend.views.file.operation import OperationView

urlpatterns = [
    path('comment/',CommentView.as_view(), name='file_comment'),
    path('operation/',OperationView.as_view(), name='file_operation'),
]