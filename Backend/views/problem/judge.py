from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Backend.models.judge_record.judge_record import SubmitRecord
from Backend.models.judge_record.judge_record import DebugRecord


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from judge_system.src.judge_server.judge_service import Judge
import json
class JudgeView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        # try:
        data=request.POST
        back = ''
        if data.get('code_judge_type') == 'submit':
            submit_record = SubmitRecord.objects.create(code = data.get('problem_content_code'))
            submit_record_id = submit_record.id
            other={
                'record_id':submit_record_id,               
            }
            back = send_judge(json.dumps(data),json.dumps(other))
            submit_record = SubmitRecord.objects.filter(id = submit_record_id)
            submit_record.update(status = back)
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
        # except:
        #     return Response({
        #         'result': "输入参数错误"
        #     })
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
