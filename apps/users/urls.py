from django.conf.urls import url

from apps.users import views

urlpatterns = [
    url('^login/',views.LoginView.as_view()),
    url('^user_info_ru/', views.UserInfoRUView.as_view()),
    url(r'^user_create/', views.UserCreateView.as_view()),
    url(r'^delivery_address_lc/$', views.DeliveryAddressLCView.as_view()),
    url(r'^delivery_address_rud/(?P<pk>[0-9]+)/$', views.DeliveryAddressRUDView.as_view())
]