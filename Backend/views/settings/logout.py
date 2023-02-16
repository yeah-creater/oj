from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import logout


class LogoutView(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response({
                    'result':'success',
                })
            else:
                logout(request)# 将该用户从数据库中退出
                return Response({
                    'result':'success',
                })
        except:
            return Response({
                'result': "error",
            })
            
