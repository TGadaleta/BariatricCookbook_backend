from django.urls import path
from .views import GenerateMealPlanView

urlpatterns = [
    path('generate-meal-plan/', GenerateMealPlanView.as_view(), name='generate_meal_plan'),
]
