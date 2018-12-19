from django.urls import path

from .apis import *

urlpatterns = [
    path('auth-token/', AuthTokenView.as_view()),
    path('profile/', ProfileView.as_view()),
]
