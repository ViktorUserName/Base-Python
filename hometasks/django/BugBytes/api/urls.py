from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='product_list'),
    path('products/info/', views.ProductInfoAPIView.as_view(), name='product_info'),
    path('orders/', views.OrderListAPIView.as_view(), name='order_list'),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user_order_list'),

]