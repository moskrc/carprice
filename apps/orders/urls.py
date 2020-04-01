from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import api_views

urlpatterns = [
    path('', csrf_exempt(api_views.OrderViewSet.as_view({'post': 'create'}))),
]
