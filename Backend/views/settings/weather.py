from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.utils.weather import weather
import json
class WeatherView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        ip = request.META.get('REMOTE_ADDR')
        res = weather(ip)
        return Response({
            'result':'success',
            'data':res
        })