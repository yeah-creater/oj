from Backend.models.solution.solution import Solution
from Backend.models.solution.serializers import SolutionListSerializer
from rest_framework import filters
from rest_framework import generics
from Backend.models.user.user import UserInfo
class SearchView(generics.ListAPIView):

    queryset = Solution.objects.filter(show = True)
    #serizlizer_class = SolutionListSerializer
    # for i in range(0, queryset.count()):
    #     user_info = UserInfo.objects.get(user_id = queryset[i].user_id)
    #     queryset[i].user_info_name = user_info.name
    #     queryset[i].user_info_photo = user_info.photo
    serializer_class = SolutionListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'file__content','user_id','problem__title']
