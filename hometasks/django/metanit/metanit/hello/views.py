from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from hello.models import Product


class ProductView(ListView):
    model = Product
    template_name = 'hello/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'hello/indexId.html'
    context_object_name = 'product'
