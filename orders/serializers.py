from rest_framework import serializers
from .models import Order, OrderItem
from products.serializer import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    # برای نمایش نام و مشخصات پایه محصول به جای فقط یک ID
    product_name = serializers.CharField(source='product.name', read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity * obj.price


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_order_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'total_order_price', 'items']
        read_only_fields = ['user', 'status']

    def get_total_order_price(self, obj):
        return sum(item.quantity * item.price for item in obj.items.all())