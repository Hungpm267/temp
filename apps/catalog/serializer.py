



from rest_framework import serializers
from .models import Product, ProductImage, Category


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
                  'categories', 'created_at', 'updated_at']
        
            




