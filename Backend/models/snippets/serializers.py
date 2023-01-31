from rest_framework import serializers
from Backend.models.snippets.snippet import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'