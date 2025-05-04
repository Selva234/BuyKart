# from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import *
from base.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
