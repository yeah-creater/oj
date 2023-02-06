from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.cache import cache
class ChangePasswordView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        # try:
        user_id = request.user.id
        data = request.POST
        row_password = data.get("row_password", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        user = User.objects.get(id = user_id)
        if not row_password or not password:
            return Response({
                'result': "密码不能为空"
            })
        if not user.check_password(row_password):
            return Response({
            'result': "原始密码不正确"
            })
        if password != password_confirm:
            return Response({
            'result': "两次密码不一致"
            })
        if len(password)<8:
            return Response({
                'result': "密码不低于8位"
            })

        user.set_password(password)
        user.save()
        return Response({
            'result': "success"
        })
        # except:
        #     return Response({
        #         'result': "输入参数错误"
        #     })
