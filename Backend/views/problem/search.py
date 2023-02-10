from Backend.models.problem.problem import Problem
from Backend.models.problem.serializers import ProblemListSerializer
from rest_framework import filters
from rest_framework import generics

class SearchView(generics.ListAPIView):

    queryset = Problem.objects.filter(show = True)
    serializer_class = ProblemListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description','tags']
