from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.contest.contest import Contest
from Backend.models.contest.serializers import ContestSerializer
import math
from django.utils import timezone  
  

class ContentView(APIView):
    def get(self, request):
        contest_id = request.GET.get('contest_id')
        now = timezone.now()
        contest = Contest.objects.get(id = contest_id)
        status = 0
        if now <= contest.start_time:
            status = 1
        elif now <= contest.over_time:
            status = 2
        else:
            status = 3
        return Response({
            'result':'success',
            'data':ContestSerializer(contest).data,
            'status':status,
        })
    
