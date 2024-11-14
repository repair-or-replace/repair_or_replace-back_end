from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

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
            # Successful login, you can add token or session handling here
            return Response(
                {'message': 'Login successful'},
                status=status.HTTP_200_OK
            )
        else:
            # Invalid credentials
            return Response(
                {'message': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
