from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.drf_generic_cbv import *
from ..views.user import *

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
