from django.conf.urls import url
from apps.orders import views
urlpatterns = [
    url(r'^cart_list/', views.CartListView.as_view()),
    url(r'^order_list/', views.OrderListView.as_view()),
    url(r'^order_create/', views.OrderCreateView.as_view()),

]