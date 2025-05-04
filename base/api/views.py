from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product
from .serializers import ProductSerializer
from base.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/products',
        'GET /api/products/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    rooms = Product.objects.all()
    serializer = ProductSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    room = Product.objects.get(id=pk)
    serializer = ProductSerializer(room, many=False)
    return Response(serializer.data)