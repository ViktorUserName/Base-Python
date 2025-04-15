from django.contrib import admin
from django.urls import path

from hello.views import ProductView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
