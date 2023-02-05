from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.conf import settings
import os
class UploadTestCaseView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        # try:
        problem_id = request.POST.get('problem_id')
        files = request.FILES.getlist('file')
        for file in files:
            path = ''
            if file.name.endswith('.in'):
                path = settings.TEST_CASE_PATH + str(problem_id) + '/in/'
                if not os.path.exists(path):
                    os.makedirs(path)
            elif file.name.endswith('.out'):
                path = settings.TEST_CASE_PATH + str(problem_id) + '/out/'
                if not os.path.exists(path):
                    os.makedirs(path)
            # 表示以二进制写方式打开,只能写文件, 如果文件不存在,创建该文件;如果文件已存在,则覆盖写
            destination = open(path + file.name, 'wb+')    
            for chunk in file.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
        
        return Response({
            'result': "success"
        })
        # except:
        #     return Response({
        #         'result': "输入参数错误"
        #     })
