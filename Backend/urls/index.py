from django.urls import path,include
from Backend.views.index import index

urlpatterns = [
   path("oj/",index,name="index"),
   path("api/",include("Backend.urls.api.index")),
   path("settings/",include("Backend.urls.settings.index")),
   path("problem/",include("Backend.urls.problem.index")),
   path("submit_record/",include("Backend.urls.submit_record.index")),
   path("user/",include("Backend.urls.user.index")),
   path("solution/",include("Backend.urls.solution.index")),
   path("blog/",include("Backend.urls.blog.index")),
   path("file/",include("Backend.urls.file.index")),
   path("video/",include("Backend.urls.video.index")),
   path("chat/",include("Backend.urls.chat.index")),
   path("contest/",include("Backend.urls.contest.index")),
]