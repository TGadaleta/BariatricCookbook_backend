from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, CustomTokenObtainSerializer

# Get the user model
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    """
    API view for user registration.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainView(TokenObtainPairView):
    """Customize JWT response to only return the access token."""
    serializer_class = CustomTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        # Remove refresh token from response
        if "refresh" in response.data:
            del response.data["refresh"]
        
        return response

@api_view(["POST"])
def logout_view(request):
    """
    Logout endpoint (placeholder since no refresh tokens exist).
    """
    return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)