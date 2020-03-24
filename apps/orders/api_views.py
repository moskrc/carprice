from rest_framework import permissions, viewsets
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    http_method_names = [
        "post",
    ]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = None
    permission_classes = (permissions.AllowAny,)
