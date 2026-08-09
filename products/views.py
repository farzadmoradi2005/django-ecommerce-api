from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Category
from .serializer import CategorySerializer,ProductSerializer
# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
