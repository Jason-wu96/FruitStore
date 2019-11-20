from apps.goods import models

from rest_framework.pagination import LimitOffsetPagination

from rest_framework import generics

from rest_framework.filters import OrderingFilter, SearchFilter

from apps.goods.serializers import GoodsSerializers


class GoodsListView(generics.ListAPIView):
    """
    商品列表
    """
    queryset = models.Goods.objects.all()
    serializer_class = GoodsSerializers
    # 按字段过滤
    filter_backends = (OrderingFilter,SearchFilter)
    search_fields = ('price','name')
    # 按字段排序
    ordering_fields = ('price','good_type' )
    ordering = ('id',)
    pagination_class = LimitOffsetPagination


class GoodsListByCategory(generics.ListAPIView):
    """
    商品分类列表
    """
    serializer_class = GoodsSerializers
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('price','good_type')
    ordering = ('-id',)

    def get_queryset(self):
        category = self.request.query_params.get('category',None)
        if category:
            queryset = models.Goods.objects.filter(good_type=category)
        else:
            queryset = models.Goods.objects.all()
        return queryset


class GoodeDetailView(generics.RetrieveAPIView):
    """
    商品详细
    """
    queryset = models.Goods.objects.all()
    serializer_class = GoodsSerializers


