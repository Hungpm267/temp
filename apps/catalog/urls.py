# apps/catalog/urls.py

from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView
)
from .views import (
    # ... Các view của Category ...
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/add/', CategoryCreateView.as_view(), name='category-add'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    
    
    # ======== THÊM CÁC URLS CHO PRODUCT DƯỚI ĐÂY ========
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]