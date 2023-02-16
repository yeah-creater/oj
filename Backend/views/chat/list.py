from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.user.user import UserInfo
from Backend.models.chat.chat import ChatList
from Backend.models.chat.serializers import ChatListSerializer
from django.utils.timezone import now
class ListView(APIView):
    permission_classes = ([IsAuthenticated])
    def get(self, request):
        try:
            user_id = request.user.id
            lists = ChatList.objects.filter(source = user_id)
            data = ChatListSerializer(lists, many=True).data
            return Response({
                'result':'success',
                'data':data,
            })
        except:
            return Response({
                'result': "error",
            })
    def post(self, request):
        try:
            source = request.user.id
            target = request.POST.get('target')
            lists = ChatList.objects.filter(source_id = source, target_id = target)
            if lists.exists():
                lists.delete()
                ChatList.objects.create(source_id = source, target_id = target)
            else:
                ChatList.objects.create(source_id = source, target_id = target)

            return Response({
                'result':'success',
            })
        except:
            return Response({
                'result': "error",
            })
