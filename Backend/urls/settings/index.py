from django.urls import path,include
from Backend.views.settings.getinfo import GetInfo

urlpatterns = [
    path('getinfo/', GetInfo.as_view(), name='settings_getinfo'),

]