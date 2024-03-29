from django.urls import path,include
from Backend.views.settings.getinfo import GetInfoView
from Backend.views.settings.logout import LogoutView
from Backend.views.settings.register import RegisterView
from Backend.views.settings.image_code import ImageCodeView
from Backend.views.settings.change_password import ChangePasswordView
from Backend.views.settings.send_email import SendEmailView
from Backend.views.settings.weather import WeatherView
urlpatterns = [
    path('getinfo/', GetInfoView.as_view(), name='settings_getinfo'),
    path('logout/', LogoutView.as_view(), name='settings_logout'),
    path('register/', RegisterView.as_view(), name='settings_register'),
    path('image_code/',ImageCodeView.as_view(),name="settings_image_code"),
    path('change_password/',ChangePasswordView.as_view(),name="settings_change_password"),
    path('send_email/',SendEmailView.as_view(),name="settings_send_email"),
     path('weather/',WeatherView.as_view(),name="settings_weather"),
]