from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Backend.models.solution.solution import Solution
from Backend.models.problem.problem import Problem
from Backend.models.user.user import UserInfo
from Backend.models.file.file import File
import math
class OperationView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        # try:
        data = request.POST
        user_id = request.user.id
        if data.get('problem_id').strip() == '' or data.get('title').strip() == '':
            return Response({
                'result': "请输入问题编号和标题",
            })
        problem_id = int(data.get('problem_id',""))
        title = data.get('title','').strip()
        content = data.get('content','')
        file = File.objects.create(content = content)
        problems = Problem.objects.filter(id = problem_id,show = True)
        if problems.exists():
            Solution.objects.create(file = file,user_id = user_id,title = title,problem = problems[0])
            return Response({
                'result': "success",
            })
        # except:
        #     return Response({
        #         'result': "fail",
        #         'data':'输入参数错误',
        #     })
    def delete(self, request):
        data = request.POST
        user_id = request.user.id
        solution_id = data.get('solution_id')
        solution = Solution.objects.get(id = solution_id)
        if solution.user_id != user_id:
            return Response({
            'result': "fail",
            })
        solution.show = False
        solution.save()
        return Response({
            'result': "success",
            })
    def put(self,request):
         # try:
        data = request.POST
        user_id = request.user.id
        solution_id = int(data.get('solution_id',""))
        title = data.get('title','').strip()
        content = data.get('content','')
        if not Solution.objects.filter(id = solution_id,show = True).exists():
            return Response({
                'result': "fail",
            })
        solution = Solution.objects.get(id = solution_id)
        if solution.user_id != user_id:
            return Response({
                'result': "fail",
            })
        solution.title = title
        solution.file.content = content
        solution.save()
        return Response({
                'result': "success",
            })
        