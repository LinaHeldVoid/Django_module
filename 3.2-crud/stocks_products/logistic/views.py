from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['title']
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['address', 'products']
    pagination_class = LimitOffsetPagination


@api_view(['GET'])
def test_page(request):
    return Response('Запущена тестовая страница')
