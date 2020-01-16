from django.shortcuts import render

from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserView(generics.ListCreateAPIView):
    
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
