from rest_framework import serializers
from .models import Category , Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name' , 'slug')


class ProductSerializer(serializers.ModelSerializer):
    # برای نمایش اطلاعات کامل دسته‌بندی در زمان خواندن (GET)
    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'inventory',
            'category',
            'category_id',
            'created_at'
        ]