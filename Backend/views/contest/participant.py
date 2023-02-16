from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from Backend.models.contest.contest import ContestParticipant
from Backend.models.contest.contest import Contest
from Backend.models.contest.serializers import ContestParticipantSerializer
import datetime
class ParticipantView(APIView):
    def get(self, request):
        contest_id = request.GET.get('contest_id')
        participants = ContestParticipant.objects.filter(contest_id = contest_id)
        data = ContestParticipantSerializer(participants, many=True).data
        return Response({
            'result':'success',
            'data':data,
        })
    def post(self,request):
        permission_classes = ([IsAuthenticated])
        user_id = request.user.id
        contest_id = request.POST.get('contest_id')
        if not ContestParticipant.objects.filter(user_id = user_id,contest_id = contest_id).exists():
            ContestParticipant.objects.create(user_id = user_id,contest_id = contest_id)
        return Response({
            'result':'success',
        })
