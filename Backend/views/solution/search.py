from Backend.models.solution.solution import Solution
from Backend.models.solution.serializers import SolutionSearchSerializer
from rest_framework import filters
from rest_framework import generics
from Backend.models.user.user import UserInfo
class SearchView(generics.ListAPIView):

    queryset = Solution.objects.filter(show = True)
    serializer_class = SolutionSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'file__content','user_id','problem__title']
