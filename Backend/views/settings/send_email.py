from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.utils.send_email import send
class SendEmailView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            username = request.GET.get('username')
            emails=[username]
            send(emails)
            return Response({
                'result':'success',
            })
        except:
            return Response({
                'result':'格式错误',
            })