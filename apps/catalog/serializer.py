



from rest_framework import serializers
from .models import Product, ProductImage, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'image']
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']
        
        
class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True, read_only =True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'thumbnail',
                  'categories', 'image', 'created_at', 'updated_at']
        
class CommentSerializer(serializers.ModelSerializer):
    # Hiển thị username thay vì user ID, và chỉ cho phép đọc
    user = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'product', 'content', 'created_at']
        # product và user sẽ được gán tự động trong view, không cần người dùng nhập
        read_only_fields = ['product', 'user']