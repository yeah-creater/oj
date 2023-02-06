from django.urls import path,include
from Backend.views.settings.getinfo import GetInfoView
from Backend.views.settings.register import RegisterView
from Backend.views.settings.image_code import ImageCodeView
from Backend.views.settings.change_password import ChangePasswordView
urlpatterns = [
    path('getinfo/', GetInfoView.as_view(), name='settings_getinfo'),
    path('register/', RegisterView.as_view(), name='settings_register'),
    path('image_code/',ImageCodeView.as_view(),name="settings_image_code"),
    path('change_password/',ChangePasswordView.as_view(),name="settings_change_password"),
]