from rest_framework import serializers
from .models import Profile, Allergy

class AllergySerializer(serializers.ModelSerializer):
    """Serializer for predefined allergy choices."""
    class Meta:
        model = Allergy
        fields = ['id', 'name']

class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the Profile model with allergy selection."""
    allergies = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Allergy.objects.all()
    )

    class Meta:
        model = Profile
        fields = ['id', 'user', 'allergies']
