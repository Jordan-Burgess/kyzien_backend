from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import User
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer, SeekerProfileSerializer, ProviderProfileSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class SeekerProfileView(APIView):
    def post(self, request, id):
        request.data['user'] = id
        serializer = SeekerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

class Users(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)