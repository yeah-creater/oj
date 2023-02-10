from Backend.models.blog.blog import Blog
from Backend.models.blog.serializers import BlogListSerializer
from rest_framework import filters
from rest_framework import generics

class SearchView(generics.ListAPIView):

    queryset = Blog.objects.filter(show = True)
    serializer_class = BlogListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','tags','file__content','user_id']
