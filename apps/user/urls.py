


from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import registerView, logoutView, profileView


urlpatterns = [
    path('register/', registerView.as_view(), name = 'register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', profileView.as_view(), name='profile'),
    path('logout/', logoutView.as_view(), name='logout')
    
]
