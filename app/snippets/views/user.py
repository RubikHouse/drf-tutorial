from django.contrib.auth.models import User
from rest_framework import generics

from snippets.serializers import UserDetailSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
