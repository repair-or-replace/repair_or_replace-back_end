from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token  # Import the Token model
from django.contrib.auth import authenticate
from rest_framework import status


class LoginView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        # Retrieve username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate inputs
        if not username or not password:
            return Response(
                {'message': 'Username and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate or get the token
            token, created = Token.objects.get_or_create(user=user)
            return Response({"message": "Login successful", "token": token.key}, status=200)
        else:
            return Response({"message": "Invalid credentials"}, status=401)