from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the healthymeal index.")

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensures only logged-in users access this
def get_profile(request):
    profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)