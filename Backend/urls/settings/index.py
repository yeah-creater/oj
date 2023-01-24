from django.urls import path,include
from Backend.views.settings.getinfo import GetInfoView
from Backend.views.settings.register import RegisterView

urlpatterns = [
    path('getinfo/', GetInfoView.as_view(), name='settings_getinfo'),
     path('register/', RegisterView.as_view(), name='settings_register'),
]