import django_filters
from django.shortcuts import render
from rest_framework import viewsets , filters
from .models import Product,Category
from django_filters.rest_framework import DjangoFilterBackend , FilterSet , NumberFilter
from .serializer import CategorySerializer,ProductSerializer
from .permissions import IsAdminOrReadOnly
# Create your views here.
class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name='price',lookup_expr='gte')
    max_price = NumberFilter(field_name='price',lookup_expr='lte')
    class Meta:
        model = Product
        fields = ['category','min_price','max_price']
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # اتصال کلاس فیلتر سفارشی
    filterset_class = ProductFilter

    # فیلدهای قابل جستجوی متنی (شامل نام و توضیحات)
    search_fields = ['name', 'description']

    # فیلدهای قابل مرتب‌سازی
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']  # پیش‌فرض: جدیدترین محصولات