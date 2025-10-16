from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

# Tạo router và đăng ký UserViewSet
router = DefaultRouter()
router.register(r'', views.UserViewSet) # Đăng ký với tiền tố rỗng

urlpatterns = [
    # Các URL cho ViewSet (sẽ tự động tạo /signup/ và /me/)
    path('', include(router.urls)),

 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Đổi tên file serializer của bạn từ serializer.py thành serializers.py để tuân thủ quy ước chung.