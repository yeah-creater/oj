from Backend.models.blog.blog import Blog
from Backend.models.blog.serializers import BlogSearchSerializer
from rest_framework import filters
from rest_framework import generics

class SearchView(generics.ListAPIView):

    queryset = Blog.objects.filter(show = True)
    serializer_class = BlogSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','tags','file__content','user_id']
