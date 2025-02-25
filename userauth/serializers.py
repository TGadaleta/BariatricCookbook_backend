from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    """
    Custom serializer that only returns an access token, removing the refresh token.
    """
    def validate(self, attrs):
        data = super().validate(attrs)  # Call the parent class's validate method

        # Retrieve the user from self.user
        user = self.user

        # Generate only the access token
        access_token = AccessToken.for_user(user)
        
        return {"access": str(access_token)}
    
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model to retrieve user details.
    """
    class Meta:
        model = User
        fields = ['id', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        """Create and return a new user with encrypted password."""
        password = validated_data.pop("password")  # Remove password from validated_data
        user = User.objects.create_user(password=password, **validated_data)  # Pass extra fields if needed
        return user
