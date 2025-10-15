# apps/catalog/models.py

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# (Class Category của bạn giữ nguyên ở đây)
class Category(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

# ======== THÊM 2 MODEL MỚI DƯỚI ĐÂY ========

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='products/thumbnails/', help_text="Ảnh đại diện cho sản phẩm")
    categories = models.ManyToManyField(Category, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"