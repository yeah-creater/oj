from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.contest.contest import Contest
from Backend.models.contest.serializers import ContestSerializer
from rest_framework.pagination import PageNumberPagination
import math
import datetime
class ListView(APIView):
    def get(self, request):
        now = datetime.datetime.now()
        contests = Contest.objects.all()
        upcoming_contests = contests.filter(over_time__gt = now)
        data1 = ContestSerializer(upcoming_contests, many=True).data
        past_contests = contests.filter(over_time__lte = now)
        pg = PageNumberPagination()
        past_contests = pg.paginate_queryset(past_contests, request)
        data2 = ContestSerializer(past_contests, many=True).data
        if request.GET.get('type') == 'upcoming':
            return Response({
                'result':'success',
                'data':data1
            })
        else:
            return Response({
                'result':'success',
                'total':(int)(math.ceil(len(past_contests)/pg.page_size)*10),
                'data':data2
            })
    
