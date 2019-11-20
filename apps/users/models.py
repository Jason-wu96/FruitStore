from django.db import models


class UserInfo(models.Model):
    """
    用户信息
    """
    username= models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    name = models.CharField(max_length=32, verbose_name='真实姓名')
    gender_choice = (
        (1, '男'),
        (2, '女'),
    )
    gender_id = models.IntegerField(choices=gender_choice,default=1, verbose_name='性别')
    birthday = models.DateField(verbose_name= '出生日期')
    phone = models.IntegerField(verbose_name='手机号')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    delivery_address = models.ForeignKey(to='DeliveryAddress', related_name='user_delivery_address',
                                         on_delete=models.CASCADE, blank=True, null=True, )

    def __str__(self):
        return self.name

class UserToken(models.Model):
    """
    Token
    """
    user = models.OneToOneField(UserInfo,on_delete=models.CASCADE,related_name='user_token')
    token = models.CharField(max_length=32)

class DeliveryAddress(models.Model):
    """
    收货地址
    """
    user = models.OneToOneField(to=UserInfo, on_delete=models.CASCADE)
    content_person = models.CharField(max_length=32, verbose_name= '联系人')
    content_phone = models.IntegerField(verbose_name='联系人电话')
    delivery_address = models.CharField(max_length=100, verbose_name='联系人地址')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.delivery_address
