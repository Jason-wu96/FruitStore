from rest_framework import serializers

from apps.users.models import *


class UserInfoSerializers(serializers.ModelSerializer):
    """
    序列化用户信息
    """
    gender = serializers.CharField(source='get_gender_id_display')
    class Meta:
        model = UserInfo
        fields = ['id','username','name','gender','birthday','phone',]


class UserSerializer(serializers.ModelSerializer):
    """
    序列化创建用户信息
    """
    class Meta:
        model = UserInfo
        fields = ('id', 'username', 'password','name','gender_id','birthday','phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserInfo(**validated_data)  # 接受前端传过来的用户名和密码
        user.save()  # 保存到内存中
        return user


class DeliveryAddressSerializer(serializers.ModelSerializer):
    """
    收货地址序列化
    """
    class Meta:
        model = DeliveryAddress
        fields = ['id','user','content_person','content_phone','delivery_address' ]
        read_only_fields = ('user',)  # 只读，不能修改



