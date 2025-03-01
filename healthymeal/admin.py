from django.contrib import admin
from .models import Profile, Allergy

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "dietary_preference", "health_goal"]
    filter_horizontal = ("allergies",)  # ✅ Allows allergy selection without auto-assigning

    def save_model(self, request, obj, form, change):
        """Ensure allergies are not auto-assigned when creating a profile."""
        if not change:  # Only applies when creating a new profile
            obj.allergies.clear()  # ✅ Explicitly removes any pre-assigned allergies
        super().save_model(request, obj, form, change)

admin.site.register(Allergy)