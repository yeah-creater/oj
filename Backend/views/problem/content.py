from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.problem.problem import Problem
from Backend.models.problem.serializers import ProblemSerializer
class ContentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            problem_content_id = int(request.GET.get('problem_content_id', 1))
            problem = Problem.objects.get(id = problem_content_id)
            serializer = ProblemSerializer(problem)
            return Response(serializer.data)
        except:
            return Response({
                'result': "输入参数错误"
            })
