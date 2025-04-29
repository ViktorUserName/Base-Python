from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProductSerializer, OrderSerializer
from api.models import Product, Order


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)