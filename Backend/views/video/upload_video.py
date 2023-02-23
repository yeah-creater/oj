from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.conf import settings
import os
from Backend.models.video.video import Video
from Backend.models.file.file import File
class UploadVideoView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        # try:
        user = request.user
        if not user.is_superuser:
            return Response({
                'result': "fail"
            })
        problem_id = request.POST.get('problem_id')
        files = request.FILES.getlist('file')
        title = '文件资源'
        for file in files:
            if not file.name.endswith('.mp4'):
                return Response({
                    'result': "success"
            })
            title = file.name[0:file.name.index('.')]
            path = settings.VIDEO_PATH
            url_content = 'https://app2105.acapp.acwing.com.cn/media/video/'+file.name
            # 表示以二进制写方式打开,只能写文件, 如果文件不存在,创建该文件;如果文件已存在,则覆盖写
            destination = open(path + file.name, 'wb+')    
            for chunk in file.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
        file = File.objects.create(content = url_content)
        Video.objects.create(file = file,user_id = user.id, title = title,problem_id = problem_id)
        return Response({
            'result': "success"
        })
        # except:
        #     return Response({
        #         'result': "error"
        #     })
