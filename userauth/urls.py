from django.urls import path
from .views import logout_view, UserCreateView, login_view, check_authentication

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('check-auth/', check_authentication, name='check-auth'),
]