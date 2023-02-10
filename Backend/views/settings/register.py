from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from Backend.models.user.user import UserInfo
from Backend.utils.located import located
from django.core.cache import cache
class RegisterView(APIView):
    permission_classes = ([AllowAny])

    def post(self, request):
        try:
            data = request.POST
            username = data.get("username", "").strip()
            password = data.get("password", "").strip()
            password_confirm = data.get("password_confirm", "").strip()
            code = data.get('code',"").strip()
            valid_code = cache.get(username,'66666')
            if not username or not password or not code:
                return Response({
                    'result': "用户名和密码不能为空"
                })
            if code.lower() != valid_code.lower():
                return Response({
                    'result': "验证码错误或已过期"
                })
            if len(password)<8:
                return Response({
                    'result': "密码不低于8位"
                })
            if password != password_confirm:
                return Response({
                    'result': "两个密码不一致",
                })
            if User.objects.filter(username=username).exists():
                return Response({
                    'result': "用户名已存在"
                })
            user = User(username=username)
            user.set_password(password)
            user.save()
            ip = request.META.get('REMOTE_ADDR')
            UserInfo.objects.create(user = user,name = 'Trainee'+str(user.id), address = located(ip))
            cache.set('access','true',30)
            return Response({
                'uuid':'access',
                'code':'true',
                'result': "success",
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
