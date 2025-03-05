from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
import json

# Get the user model
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    """
    API view for user registration.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

@csrf_exempt
def login_view(request):
    """
    API view for user login.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful."})
        else:
            return JsonResponse({"message": "Invalid credentials."})
    return JsonResponse({"message": "Invalid method."})

@csrf_exempt
def logout_view(request):
    """
    API view for user logout.
    """
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logout successful."})
    return JsonResponse({"message": "Invalid method."})

def check_authentication(request):
    """
    Function to check if a user is authenticated.
    """
    if request.user.is_authenticated:
        return JsonResponse({"authenticated": True, "user": request.user.email}, status=200)
    else:
        return JsonResponse({"authenticated": False}, status=401)