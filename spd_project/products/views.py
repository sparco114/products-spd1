from django.shortcuts import render

from products.models import Product
from rest_framework.viewsets import ModelViewSet

from products.serializers import ProductSerializer


def products_page(request):
    return render(request=request, template_name='products.html', context={'prod1': Product.objects.all()[0],
                                                                           'prod2': Product.objects.all()[1],
                                                                           })


class ProductsView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
