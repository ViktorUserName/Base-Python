from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product_list'),
    path('orders/', views.OrderListAPIView.as_view(), name='order_list'),
    path('products/info/', views.product_info, name='product_info'),
]