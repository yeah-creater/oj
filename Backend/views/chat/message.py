from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.user.user import UserInfo
from Backend.models.chat.chat import ChatMessage
from Backend.models.chat.serializers import ChatMessageSerializer
from Backend.models.chat.chat import ChatList
import math
class MessageView(APIView):
    permission_classes = ([IsAuthenticated])
    def get(self, request):
        # try:
        source = request.user.id
        target = request.GET.get('target')
        list1 = ChatMessage.objects.filter(source = source, target = target)
        list2 = ChatMessage.objects.filter(source = target, target = source)
        lists = list1 | list2
        data = ChatMessageSerializer(lists, many=True).data
        return Response({
            'result':'success',
            'data':data,
        })
        # except:
        #     return Response({
        #         'result': "fail",
        #         'data':'输入参数错误',
        #     })
    def post(self, request):
        # try:
        source = request.user.id
        target = request.POST.get('target')
        content = request.POST.get('content')
        meg = ChatMessage.objects.create(source_id = source,target_id =target,content=content)
        if not ChatList.objects.filter(source_id = source,target_id = target).exists():
            ChatList.objects.create(source_id = source, target_id = target)
        if not ChatList.objects.filter(source_id = target,target_id = source).exists():
            ChatList.objects.create(source_id = target, target_id = source)
        return Response({
            'result':'success',
            'data':ChatMessageSerializer(meg).data,
        })
