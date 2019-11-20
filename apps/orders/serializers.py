from rest_framework import serializers

from apps.orders.models import *

class OrderListSerializer(serializers.ModelSerializer):
    """
    序列化订单列表
    """
    product = serializers.CharField(source='goods.name')
    address = serializers.CharField(source='address.delivery_address')

    class Meta:
        model = Order
        fields = ('id', 'status', 'user', 'goods', 'price', 'quantity', 'remark', 'address', 'created', 'updated',)


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    序列化创建订单
    """
    goods = serializers.CharField(source='goods.name')
    address = serializers.CharField(source='address.delivery_address')
    class Meta:
        model = Order
        fields = ('id', 'status', 'user', 'goods', 'price', 'quantity', 'remark', 'address', 'created', 'updated',)
        read_only_fields = ('user', 'price', 'address',)
