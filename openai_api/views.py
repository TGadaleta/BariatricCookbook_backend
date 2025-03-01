from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
import os
from .serializers import MealPlanSerializer

class GenerateMealPlanView(APIView):
    def post(self, request):
        serializer = MealPlanSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        user_preferences = validated_data.get("preferences", {})
        days = validated_data["days"]
        meals_per_day = validated_data["meals_per_day"]

        prompt = f"Generate a {days}-day meal plan with {meals_per_day} meals per day based on the following preferences: {user_preferences}."

        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="gpt-4o",
)   
            meal_plan = response.choices[0].message.content.strip()

            return Response({"meal_plan": meal_plan}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

