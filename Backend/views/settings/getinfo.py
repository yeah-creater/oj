from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GetInfo(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id', 1))
            return Response({
                'id': user_id,
                'username': 'xx',
                'photo': 'xx',
                'followerCount': 11,
                'is_followed': True,
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
