from django.db import models

from apps.goods.models import Goods
from apps.users.models import UserInfo, DeliveryAddress


class Order(models.Model):
    """
    订单
    """
    STATUS_CHOICES = (
        ('0', 'new'),
        ('1', 'not paid'),
        ('2', 'paid'),
        ('3', 'transport'),
        ('4', 'closed'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='0', max_length=2)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='order_of',)
    remark = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Goods, related_name='order_product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    address = models.ForeignKey(DeliveryAddress, related_name='order_address', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)