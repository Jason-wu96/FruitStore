from rest_framework import generics

from rest_framework.exceptions import NotFound

from apps.users.serializers import UserInfoSerializers, UserSerializer, DeliveryAddressSerializer

from apps.users.models import *

from rest_framework.views import APIView

from rest_framework.response import Response

from utils.md5 import md5

from utils.auth import MyToken


class LoginView(APIView):
    """登录"""
    def post(self, request, *args, **kwargs):
        results = {
            'code': 1000,
        }
        try:
            user = request.data.get('username')
            pwd = request.data.get('password')
            user_obj = UserInfo.objects.get(username=user, password=pwd)  # 取不到和取多个都会报错
            if not user_obj:
                results['code'] = 1001
                results['error'] = '用户名或密码错误'
                return Response(results)
            token = md5(user)
            UserToken.objects.update_or_create(user=user_obj, defaults={'token': token})
            results['token'] = token
        except Exception as e:
            results['code'] = 1003
        return Response(results)


class UserInfoRUView(generics.RetrieveUpdateAPIView):
    """
    用户个人信息，可进行修改
    """

    serializer_class = UserInfoSerializers
    authentication_classes = [MyToken]
    def get_object(self):
        token = self.request.query_params.get('token')
        print(token)
        obj = UserToken.objects.filter(token=token).first()
        ret = obj.user
        return ret

class UserCreateView(generics.CreateAPIView):
    """
    用户创建
    """
    serializer_class = UserSerializer


class DeliveryAddressLCView(generics.ListCreateAPIView):
    """
    收货地址LC
    """
    serializer_class = DeliveryAddressSerializer
    authentication_classes = [MyToken]

    def get_queryset(self):
        user = self.request.user
        queryset = DeliveryAddress.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class DeliveryAddressRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    收货地址的RUD
    """
    serializer_class = DeliveryAddressSerializer
    authentication_classes = [MyToken]

    def get_object(self):
        user = self.request.user
        try:
            obj = DeliveryAddress.objects.get(id=self.kwargs['pk'], user=user)
        except Exception as e:
            raise NotFound('no found')
        return obj


