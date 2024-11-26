from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Retrieve fields from request data
        username = request.data.get('username')
        new_password = request.data.get('new_password')
        new_password_confirm = request.data.get('new_password_confirm')

        # Check if passwords match
        if new_password != new_password_confirm:
            return Response({'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve user and update password
            user = User.objects.get(username=username)
            user.password = make_password(new_password)  # Use make_password for consistent hashing
            user.save()

            return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
