from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.OrderViewSet.as_view({'post': 'create'})),
]
