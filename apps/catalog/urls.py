# apps/catalog/urls.py


# from .views import (
#     CategoryListView,
#     CategoryDetailView,
#     CategoryCreateView,
#     CategoryUpdateView,
#     CategoryDeleteView
# )
# from .views import (
#     # ... Các view của Category ...
#     ProductListView,
#     ProductDetailView,
#     ProductCreateView,
#     ProductUpdateView,
#     ProductDeleteView
# )

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CommentViewSet
from rest_framework_nested import routers 
from django.urls import path, include

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

# Router lồng nhau cho comments
products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'comments', CommentViewSet, basename='product-comments')

urlpatterns = [
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('category/add/', CategoryCreateView.as_view(), name='category-add'),
    # path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    # path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    
    
    # # ======== THÊM CÁC URLS CHO PRODUCT DƯỚI ĐÂY ========
    # path('products/', ProductListView.as_view(), name='product-list'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    # path('product/add/', ProductCreateView.as_view(), name='product-add'),
    # path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    # path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('', include(router.urls)),
    path('', include(products_router.urls)),

]

router = DefaultRouter()
router.register(r'products', ProductViewSet)
products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'comments', CommentViewSet, basename='product-comments')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
]