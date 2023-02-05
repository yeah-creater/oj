from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.judge_record.judge_record import SubmitRecord
from Backend.models.judge_record.judge_record import DebugRecord
from Backend.models.problem.problem import Problem

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from judge_system.src.judge_server.judge_service import Judge

import json
import json
class JudgeView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        try:
            data = request.POST
            back = ''
            if data.get('code_judge_type') == 'submit':
                submit_record = SubmitRecord.objects.create(
                    user_id = request.user.id,
                    problem_id = data.get('problem_content_id'),
                    code = data.get('problem_content_code'),
                    language = data.get('problem_content_language'),
                    )
                submit_record_id = submit_record.id
                problem = Problem.objects.filter(id = data.get('problem_content_id'))
                if not problem.exists():    return ''
                problem_submit_nums = problem[0].submit_nums
                problem.update(submit_nums = problem_submit_nums + 1)
                other={
                    'record_id':submit_record_id, 
                }
                back = send_judge(json.dumps(data),json.dumps(other))
                submit_record = SubmitRecord.objects.filter(id = submit_record_id)
                status = json.loads(back).get('status')
                if status == 'Accepted':
                    problem_ac_nums = problem[0].ac_nums
                    problem.update(ac_nums = problem_ac_nums + 1)
                submit_record.update(status = status)

            else:
                debug_record = DebugRecord.objects.create(code = data.get('problem_content_code'))
                debug_record_id = debug_record.id
                other={
                    'record_id':debug_record_id,
                }
                back = send_judge(json.dumps(data),json.dumps(other))
            return Response({
                'result':'success',
                'data':back,
            })
        except:
             return Response({
                 'result': "输入参数错误"
             })
def send_judge(info,other):
    # Make socket
    transport = TSocket.TSocket('127.0.0.1',9090)
    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Judge.Client(protocol)
    # Connect!
    transport.open()
    res = client.judge_code(info,other)
    # Close!
    transport.close()
    return res
