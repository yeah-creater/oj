from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.problem.problem import Problem
from Backend.models.problem.serializers import ProblemSerializer
import markdown
EXTENTIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    'markdown.extensions.tables'
]
KEYS=('description','input_format','output_format','data_range',
'input_example','output_example')
class ContentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            problem_content_id = int(request.GET.get('problem_content_id', 1))
            problems = Problem.objects.filter(id = problem_content_id)
            if(len(problems)==0 or not problems[0].show):
                return Response({
                'result': "输入参数错误"
                })
            serializer = ProblemSerializer(problems[0])
            data = serializer.data
            for key in KEYS:
                val = data.get(key)
                data[key]=markdown.markdown(val,extensions = EXTENTIONS)
            return Response({
                'result':'success',
                'data':data,
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
