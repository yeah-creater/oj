from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoRatingSerializer
from Backend.models.contest.contest import Contest
from Backend.models.contest.contest import ContestParticipant
from Backend.models.contest.serializers import ContestParticipantSerializer
class RatingView(APIView):
    def get(self, request):
        userinfos = UserInfo.objects.all()
        data = UserInfoRatingSerializer(userinfos, many=True).data
        for i in range(0,len(data)):
            if i != 0 and data[i]['rating'] == data[i - 1]['rating']:
                data[i]['standing'] = data[i - 1]['standing']
            else:
                data[i]['standing'] = i + 1
        return Response({
            'result':'success',
            'data':data,
        })
    def post(self, request):
        permission_classes = ([IsAuthenticated])
        contest_id = request.POST.get('contest_id')
        user = request.user
        contest = Contest.objects.get(id = contest_id)
        if not user.is_superuser or contest.clear:
            return Response({
                'result':'success',
            })
        # cps = ContestParticipant.objects.filter(contest_id = contest_id)
        # for host in cps:

        #     for guest in cps:
        #         if host.user.id != guest.user.id:
        #             print(host)
        contest.clear = True
        contest.save()
        return Response({
                'result':'success',
            })
