from django.urls import path
from .views import get_profile, index

from . import views

urlpatterns = [
    path("", index, name="index"),
    path("profile/", get_profile, name="get_profile"),
]