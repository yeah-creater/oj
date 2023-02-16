from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.problem.problem import Problem
from Backend.models.problem.serializers import ProblemTitleSerializer
class TitleView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        # try:
        type = request.GET.get('type')
        if type == 'one':
            problem_content_id = int(request.GET.get('problem_id', 1))
            problems = Problem.objects.filter(id = problem_content_id)
            if(problems[0] == None or not problems[0].show):
                return Response({
                'result': "该题不存在"
                })
            serializer = ProblemTitleSerializer(problems[0])
        else:
            problems = Problem.objects.filter(show = True)
            serializer = ProblemTitleSerializer(problems, many = True)
        data = serializer.data
        return Response({
            'result':'success',
            'data':data,
        })
        # except:
        #     return Response({
        #         'result': "error"
        #     })
