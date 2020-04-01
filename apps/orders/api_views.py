from rest_framework import permissions, viewsets
from .models import Order
from .serializers import OrderSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return 

class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, )
    http_method_names = [
        "post",
    ]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = None
    permission_classes = (permissions.AllowAny,)
