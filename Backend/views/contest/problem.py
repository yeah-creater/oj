from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from Backend.models.problem.problem import Problem
from Backend.models.problem.problem import AcProblem
from Backend.models.problem.serializers import ProblemSerializer
from Backend.models.contest.contest import Contest
from Backend.models.contest.contest import ContestParticipant
from Backend.models.contest.serializers import ContestSerializer
import math
import datetime
class ProblemListView(APIView):
    permission_classes = ([IsAuthenticated])
    def get(self, request):
        now = datetime.datetime.now()
        # 可以返回:该竞赛开始时间小于等于现在并且当前用户已报名
        user_id = request.user.id
        contest_id = request.GET.get('contest_id')
        r1 = Contest.objects.filter(id = contest_id,start_time__lte = now)
        r2 = ContestParticipant.objects.filter(user_id = user_id,contest_id = contest_id)
        if r1 and r2:
            problems = Problem.objects.filter(contest = contest_id)
            data = ProblemSerializer(problems,many=True).data
            for i in range(0,len(data)):
                data[i]['status'] = '未通过'
                problem_id = data[i]['id']
                if AcProblem.objects.filter(problem_id = problem_id,user_id = user_id).exists():
                    data[i]['status'] = '通过'
            return Response({
                'result':'success',
                'data':data,
            }) 
        # 否则就不可以返回
        return Response({
            'result':'success',
            'data':[],
        })
    
