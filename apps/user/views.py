# from django.shortcuts import render, redirect, get_object_or_404
# from rest_framework.views import APIView
# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework import status

# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
   
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save() # create new user form form
#             login(request, user) # tu dong signin cho user sau khi signup
#             return redirect('profile')
#     else:
#         form = UserCreationForm() # tao form dang ki trong
#     return render(request, 'user/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data = request.POST) #khi user an nut login
#         if form.is_valid():
#             user = form.get_user() # lay username va password tu form
#             login(request, user)
#             return redirect('profile')
#     else:
#         form = AuthenticationForm() # tao form dangnhap trong
    
#     return render(request, 'user/login.html', {'form' : form})
        
# @login_required(login_url='login')
# def profile_view(request):
#     return render(request, 'user/profile.html')

# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login')


# ====================================================================

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer

class UserViewSet(mixins.CreateModelMixin, # Chỉ cho phép hành động 'create' (đăng ký)
                  viewsets.GenericViewSet): # Không có các hành động 'list', 'retrieve' mặc định
    """
    ViewSet để xử lý đăng ký và xem thông tin người dùng.
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            print("tạo user mới và chạy vào register serializer ")
            return RegisterSerializer
        print("chạy vào user serializer ")
        return UserSerializer

    def get_permissions(self):
        """
        Gán quyền cho từng hành động:
        - Ai cũng có thể 'create' (đăng ký).
        - Phải đăng nhập để xem 'me' (thông tin cá nhân).
        """
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='me')
    def get_current_user_profile(self, request):
        """
        Endpoint tùy chỉnh để lấy thông tin của user đã đăng nhập.
        URL: /user/me/
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)