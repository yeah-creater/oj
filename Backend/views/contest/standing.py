from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.contest.contest import Contest
from Backend.models.contest.contest import ContestParticipant
from Backend.models.contest.serializers import ContestParticipantSerializer
from rest_framework.pagination import PageNumberPagination
import math
import datetime
class StandingView(APIView):
    def get(self, request):
        contest_id = request.GET.get('contest_id')
        contest_participants = ContestParticipant.objects.filter(contest_id = contest_id)
        pg = PageNumberPagination()
        res = pg.paginate_queryset(contest_participants,request)
        data = ContestParticipantSerializer(res,many = True).data
        for i in range(0,len(data)):
            data[i]['ranking'] = (int(request.GET.get('page')) - 1) * 10 + i + 1
        return Response({
            'result':'success',
            'data':data,
            'total':(int)(math.ceil(len(contest_participants)/pg.page_size)*10),
        })
