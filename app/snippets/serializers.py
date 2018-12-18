from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )


class UserDetailSerializer(UserSerializer):
    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + ('snippet_set',)


class SnippetSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Snippet
        fields = (
            'pk',
            'owner',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )
