from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer




class registerView(APIView):
    permissions_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class profileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
        