from django.http import JsonResponse
from django.core.cache import cache
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

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
   
