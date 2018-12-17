from django.urls import path, include

from . import django_fbv
from . import drf_cbv
from . import drf_fbv
from . import drf_mixin

urlpatterns = [
    path('django-fbv/', include(django_fbv)),
    path('drf-fbv/', include(drf_fbv)),
    path('drf-cbv/', include(drf_fbv)),
    path('drf-mixin/', include(drf_mixin)),
]
