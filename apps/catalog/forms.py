# apps/catalog/forms.py

from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent', 'image']
        
        
# ======== THÊM FORM MỚI DƯỚI ĐÂY ========
class ProductForm(forms.ModelForm):
    # Thêm trường này để cho phép upload nhiều file ảnh cùng lúc
    # more_images = forms.FileField(
    #     required=False,
    #     widget=forms.FileInput(attrs={'multiple': True}) 
    # )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'thumbnail', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }

