from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from Backend.models.user.user import UserInfo
from django.core.cache import cache
class RegisterView(APIView):
    permission_classes = ([AllowAny])

    def post(self, request):
        # try:
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        uuid = request.META.get('HTTP_USER_AGENT',"unknown")+request.META.get('REMOTE_HOST')
        code = data.get('code',"").strip()
        valid_code = cache.get(uuid,'66666')

        if not username or not password or not code:
            return Response({
                'result': "用户名和密码不能为空"
            })
        if code.lower() != valid_code.lower():
            return Response({
                'result': "验证码错误"
            })
        if not username.isnumeric() or len(username)!=11:
            return Response({
                'result': "用户名必须为11位数字"
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
        UserInfo.objects.create(user = user,name = 'Trainee'+str(user.id))
        return Response({
            'result': "success"
        })
        # except:
        #     return Response({
        #         'result': "输入参数错误"
        #     })
