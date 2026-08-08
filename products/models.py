from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField(blank=True , null=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name