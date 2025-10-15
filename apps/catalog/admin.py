# apps/catalog/admin.py

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, ProductImage

# Đăng ký Category 
admin.site.register(Category, MPTTModelAdmin)

# Dùng TabularInline để thêm nhiều ảnh ngay trên trang Product
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 # Số lượng form trống để upload ảnh mới

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('categories', 'created_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('categories',) # Giao diện dễ chọn nhiều category
    inlines = [ProductImageInline]