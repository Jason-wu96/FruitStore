from rest_framework import generics

from utils.auth import MyToken
from apps.orders.serializers import *

from apps.orders.models import *


class CartListView(generics.ListAPIView):
    """
    购物车列表
    """
    serializer_class = OrderListSerializer
    authentication_classes = [MyToken]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user, status='0')   # 购物车商品状态都是未付款，默认为0
        return queryset


class OrderListView(generics.ListAPIView):
    """
    订单列表
    """
    serializer_class = OrderListSerializer
    authentication_classes = [MyToken]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user, status__in=['1', '2', '3', '4'])
        return queryset


class OrderCreateView(generics.CreateAPIView):
    """
    创建订单
    """
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    authentication_classes = [MyToken]

    def perform_create(self, serializer):
        user = self.request.user
        goods = serializer.validated_data.get('goods')
        serializer.save(user=user, price=goods.price, address=user.profile_of.delivery_address, status='0', )
