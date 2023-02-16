from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer
from django.conf import settings
from Backend.utils.encryption import rndName
from Backend.utils.image_save import save

class ProfileView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        try:
            user_id = request.user.id
            files = request.FILES.getlist('file')
            name = rndName(8)
            for file in files:
                path = settings.MEDIA_ROOT + '/profile/'
                # 表示以二进制写方式打开,只能写文件, 如果文件不存在,创建该文件;如果文件已存在,则覆盖写
                destination = open(path + name+'.jpg', 'wb+')    
                for chunk in file.chunks():      # 分块写入文件
                    destination.write(chunk)
                destination.close()
            save(path + name + '.jpg')
            user_info = UserInfo.objects.filter(user_id = user_id)
            photo = 'https://app2105.acapp.acwing.com.cn/media/profile/' + name +'.jpg'
            user_info.update(photo = photo)
            return Response({
                'result': "success",
                'data':photo,
            })
        except:
            return Response({
                'result': "error",
            })
