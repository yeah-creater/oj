from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Backend.models.user.user import UserInfo
from Backend.models.notification.serializers import NotificationSerializer
from Backend.models.notification.notification import Notification
from rest_framework.pagination import PageNumberPagination
import math
class NotificationView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        source_id = request.user.id
        notifications = Notification.objects.filter(source_id = source_id)
        for notification in notifications:
            notification.read = True
            notification.save()
        pg = PageNumberPagination()
        res = pg.paginate_queryset(notifications,request)
        data = NotificationSerializer(res,many=True).data
        return Response({
            'result': "success",
            'data':data,
            'total': (int)(math.ceil(len(notifications)/pg.page_size)*10),
        })
