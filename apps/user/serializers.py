# from rest_framework import serializers
# from django.contrib.auth.models import User

# # Serializer để hiển thị thông tin user (an toàn)
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']

# # Serializer để đăng ký user mới (giữ nguyên)
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email', ''), # Thêm giá trị mặc định
#             password=validated_data['password']
#         )
#         return user
    
    
    # ==================================
from rest_framework import serializers
from django.contrib.auth.models import User
from .task import gui_thong_bao_co_user_moi

# Serializer để hiển thị thông tin user (an toàn)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer để đăng ký user mới (giữ nguyên)
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    print("chạy trạm")
    class Meta:
        model = User 
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email=validated_data.get('email', ''),
            password= validated_data['password']
        )
        print("sau khi chạy vào gửi thong báo")
        gui_thong_bao_co_user_moi.delay(user.username, user.email)
        
        return user