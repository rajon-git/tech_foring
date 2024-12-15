from django.shortcuts import render
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = True  
        user.save()
       
        return Response({
        "message": "User registered successfully. A verification code has been sent to your email.",
        "email": user.email
    }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid Credentials "}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.check_password(password) and user.is_active:
            # Generate or get the token
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key, 
                "user": { 
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                "message": "Login successful."
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid Credentials or account not activated."}, status=status.HTTP_400_BAD_REQUEST)
     
class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token = request.auth
        if token:
            Token.objects.filter(key=token).delete()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No token found."}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
