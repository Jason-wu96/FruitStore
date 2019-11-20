from django.contrib import admin

from apps.users.models import *

admin.site.register(UserInfo)

admin.site.register(UserToken)

admin.site.register(DeliveryAddress)