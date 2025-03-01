from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Allergy(models.Model):
    """Predefined allergy choices stored in a separate model."""
    
    ALLERGY_CHOICES = [
        ("peanuts", "Peanuts"),
        ("dairy", "Dairy"),
        ("gluten", "Gluten"),
        ("shellfish", "Shellfish"),
        ("soy", "Soy"),
        ("eggs", "Eggs"),
        ("tree_nuts", "Tree Nuts"),
        ("fish", "Fish"),
    ]

    name = models.CharField(
        max_length=50,
        choices=ALLERGY_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.get_name_display()  # Returns the readable name of the allergy

class Profile(models.Model):
    """
    User profile storing dietary preferences, allergies, and health goals.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    allergies = models.ManyToManyField(Allergy, blank=True)

    # Dietary Preferences
    DIET_CHOICES = [
        ("vegetarian", "Vegetarian"),
        ("vegan", "Vegan"),
        ("keto", "Keto"),
        ("paleo", "Paleo"),
        ("gluten_free", "Gluten-Free"),
        ("dairy_free", "Dairy-Free"),
        ("low_carb", "Low Carb"),
        ("balanced", "Balanced"),
        ("other", "Other"),
    ]
    dietary_preference = models.CharField(
        max_length=20, choices=DIET_CHOICES, default="balanced"
    )

    # Macronutrient Preferences
    calorie_goal = models.IntegerField(default=2000, help_text="Daily calorie intake goal in kcal")
    protein_percentage = models.FloatField(default=20.0, help_text="Protein percentage of daily intake")
    carbs_percentage = models.FloatField(default=50.0, help_text="Carbs percentage of daily intake")
    fat_percentage = models.FloatField(default=30.0, help_text="Fat percentage of daily intake")

    # Health Goals
    HEALTH_GOALS = [
        ("weight_loss", "Weight Loss"),
        ("muscle_gain", "Muscle Gain"),
        ("maintenance", "Maintenance"),
    ]
    health_goal = models.CharField(
        max_length=20, choices=HEALTH_GOALS, default="maintenance"
    )

    def __str__(self):
        return f"{self.user.email} - {self.dietary_preference}"

