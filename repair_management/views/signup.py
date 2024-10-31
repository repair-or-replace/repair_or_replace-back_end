from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterView(APIView):
    def post(self, request):
        # Retrieve fields from request data
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        password_confirm = request.data.get('password_confirm')

        # Check if passwords match
        if password != password_confirm:
            return Response({'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Use make_password to hash the password and create the user
        hashed_password = make_password(password)
        User.objects.create(username=username, email=email, password=hashed_password)

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

