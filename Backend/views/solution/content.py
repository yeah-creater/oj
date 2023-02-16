from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.solution.solution import Solution
from Backend.models.solution.serializers import SolutionContentSerializer
from Backend.models.user.user import UserInfo
from Backend.utils.md_to_html import md_to_html
from Backend.models.file.file import File
import math
class ContentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            solution_id = request.GET.get('solution_id')
            if not Solution.objects.filter(id = solution_id,show = True).exists():
                return Response({
                'result':'fail',
                })
            solution = Solution.objects.get(id = solution_id,show = True)
            content = solution.file.content
            data = SolutionContentSerializer(solution).data
            user_info = UserInfo.objects.get(user_id = data['user_id'])
            data['user_info_name'] = user_info.name
            data['user_info_photo'] = user_info.photo
            data['content'] = content
            if int(request.GET.get('md')) == 0:
                data['content'] = md_to_html(content)
            return Response({
                'result':'success',
                'data':data
            })
        except:
            return Response({
                'result': "error",
            })
