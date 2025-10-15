


from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import login_view, logout_view, profile_view, signup_view


urlpatterns = [
    path('signup/', signup_view, name = 'signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout')
    
]
