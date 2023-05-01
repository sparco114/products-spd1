from django.shortcuts import render

from orders.models import SalesOrder
from rest_framework.viewsets import ModelViewSet

from orders.serializers import OrderSerializer


def orders_page(request):
    return render(request=request, template_name='index.html', context={'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


