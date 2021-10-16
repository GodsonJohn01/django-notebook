from django.db.models import fields
from rest_framework import serializers
from .models import Snippet, Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for getting snippet title
    """
    class Meta:
        model = Tag
        fields = ['title']


class SnippetListSerializer(serializers.ModelSerializer):
    """
    Serializer for getting the list of snippet title
    """
    class Meta:
        model = Snippet
        fields = ['id', 'tag']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['tag'] = TagSerializer(instance.tag).data
        return rep


class SnippetCreateSerializer(serializers.Serializer):
    """
    Serializer for creating new snippet
    """
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=200, allow_blank=True)


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for getting the details of a snippet
    """
    last_modified = serializers.ReadOnlyField()

    class Meta:
        model = Snippet
        fields = ['id', 'tag', 'content', 'last_modified']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['tag'] = TagSerializer(instance.tag).data
        return rep
        