from rest_framework import serializers

from apps.goods import models


class GoodsSerializers(serializers.ModelSerializer):
    """
    序列化商品
    """
    good_type = serializers.CharField(source='good_type.name')
    class Meta:
        model = models.Goods
        fields = ['id','name','price','image','desc','good_type']

