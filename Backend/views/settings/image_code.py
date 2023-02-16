from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from Backend.utils.image_code import check_code
from io import BytesIO
from django.shortcuts import HttpResponse
from django.core.cache import cache
import base64
from Backend.utils.encryption import rndName
class ImageCodeView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            img, code_string = check_code()
            uuid = rndName(8)
            cache.set(uuid,code_string,60)
            stream = BytesIO()
            img.save(stream, 'png')
            img = base64.b64encode(stream.getvalue())
            return Response({
                'result':'success',
                'img':img,
                'uuid':uuid,
            })
        except:
            return Response({
                'result': "error"
            })
