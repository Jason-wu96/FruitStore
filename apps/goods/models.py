from django.db import models

class Category(models.Model):
    """
    商品分类
    """
    name = models.CharField(max_length=32, verbose_name='商品类别')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    name = models.CharField(max_length=32, verbose_name='商品名称')
    price = models.FloatField(max_length=12, verbose_name='价格')
    desc = models.TextField(max_length=200,verbose_name='商品描述')
    image = models.ImageField(max_length=100,upload_to='goods/upload/%Y/%m/%d/', verbose_name='商品图片')
    good_type = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
