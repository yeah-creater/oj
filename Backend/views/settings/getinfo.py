from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class GetInfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id', 1))
            user=User.objects.get(id=user_id)
            return Response({
                'id': user_id,
                'username': user.username,
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
