from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.blog.blog import Blog

from Backend.models.blog.serializers import BlogListSerializer
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
import math
class ListView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            blogs = Blog.objects.filter(show = True)
            if request.GET.get('user_id') != None:
                blogs = blogs.filter(user_id = int(request.GET.get('user_id')))
            if blogs.count() == 0:
                return Response({
                'result':'success',
                'total':0,
                'data':[],
            })
            pg = PageNumberPagination()
            res = pg.paginate_queryset(blogs, request)
            data = BlogListSerializer(res, many=True).data
            for i in range(0, len(data)):
                user_info = UserInfo.objects.get(user_id = data[i]['user_id'])
                data[i]['user_info_name'] = user_info.name
                data[i]['user_info_photo'] = user_info.photo
            return Response({
                'result':'success',
                'total':(int)(math.ceil(len(blogs)/pg.page_size)*10),
                'data':data
            })
        except:
            return Response({
                'result': "error",
            })
