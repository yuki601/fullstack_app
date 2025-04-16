from rest_framework import serializers
from .models import Product, Purchase, Sales

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields='__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields = '__all__'

class InventorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    unit = serializers.IntegerField()
    quantity = serializers.IntegerField()
    type = serializers.IntegerField()
    date = serializers.DateField()

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

class SalesSerializer(serializers.Serializer):
    monthly_date = serializers.DateTimeField(format='%Y-%m')
    monthly_price = serializers.IntegerField()