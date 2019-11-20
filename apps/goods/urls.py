from django.conf.urls import url

from apps.goods import views

urlpatterns = [
    url('^goods/', views.GoodsListView.as_view()),
    url('^goods_category/', views.GoodsListByCategory.as_view()),
    url('^goods_detail/(?P<pk>\d+)/', views.GoodeDetailView.as_view())

]