from django.urls import path, re_path
from products.views import ProductList, ProductDetail, ProductGetByCondition

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view(), name='detailcreate'),
    path('', ProductList.as_view(), name='listcreate'),
    re_path(r'^purchases/(?P<username>\w{0,50})/$', ProductGetByCondition.as_view())
]