from django.urls import path, include

from . import django_fbv, drf_cbv, drf_fbv, drf_generic_cbv, drf_mixin

urlpatterns = [
    path('django-fbv/', include(django_fbv)),
    path('drf-fbv/', include(drf_fbv)),
    path('drf-cbv/', include(drf_fbv)),
    path('drf-mixin/', include(drf_mixin)),
    path('drf-generic-cbv/', include(drf_generic_cbv)),
]
