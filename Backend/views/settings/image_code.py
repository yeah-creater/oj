from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from Backend.utils.image_code import check_code
from io import BytesIO
from django.shortcuts import HttpResponse
from django.core.cache import cache
class ImageCodeView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            img, code_string = check_code()
            uuid=request.META.get('HTTP_USER_AGENT',"unknown")+request.META.get('REMOTE_HOST')
            cache.set(uuid,code_string,100)
            stream = BytesIO()
            img.save(stream, 'png')
            return HttpResponse(stream.getvalue(),content_type='images/jpg')
        except:
            return Response({
                'result': "输入参数错误"
            })
