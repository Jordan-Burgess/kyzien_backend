from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('users/', views.Users.as_view(), name='users'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('seeker-onboarding/<int:id>/', views.SeekerProfileView.as_view(), name="seeker_onboarding"),
]