from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Profile(models.Model):
    """
    User profile storing dietary preferences, allergies, and health goals.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

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

    # Allergies (Multiple choices stored as JSON)
    ALLERGY_CHOICES = [
        ("peanuts", "Peanuts"),
        ("dairy", "Dairy"),
        ("gluten", "Gluten"),
        ("shellfish", "Shellfish"),
        ("soy", "Soy"),
        ("eggs", "Eggs"),
        ("tree_nuts", "Tree Nuts"),
        ("fish", "Fish"),
        ("none", "None"),
    ]
    allergies = models.JSONField(default=list, blank=True)

    # Meal Preferences
    MEAL_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("snacks", "Snacks"),
    ]
    preferred_meals = models.JSONField(default=list, blank=True)  # List of preferred meal types

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

    # Preferred Cuisines
    cuisine_preferences = models.JSONField(default=list, blank=True, help_text="Preferred cuisine types")

    def __str__(self):
        return f"{self.user.email} - {self.dietary_preference}"

