from django.http import JsonResponse
from django.core.cache import cache
from django.middleware.common import MiddlewareMixin
from Backend.models.log.log import Log

# 拦截器 处理登录验证码
class  InterceptorMiddleware(MiddlewareMixin):
    def process_request(self, request): 
        if request.path == ("/api/token/"):
            uuid = request.POST.get('uuid','')
            code = request.POST.get('code','')
            valid_code = cache.get(uuid,'66666')
            if code.lower() != valid_code.lower():
                return JsonResponse({
                    'result': "fail"
                })
   
class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        Log.objects.create(request_path = request.get_full_path(), content = exception)
        return JsonResponse({
                'result': "error"
            }) 