from django.urls import path,include
from Backend.views.index import index

urlpatterns = [
   path("",index,name="index"),
   path("api/",include("Backend.urls.api.index")),
   path("settings/",include("Backend.urls.settings.index")),
   path("problem/",include("Backend.urls.problem.index")),
]