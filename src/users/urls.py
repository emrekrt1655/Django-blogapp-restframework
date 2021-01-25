from django.urls import path
from .views import RegisterView,  ProfileListView, DetailedProfileView, ProfileUpdateView
from rest_framework import views as rest_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile/', ProfileListView.as_view(), name='profiles'),
    path('profile/<slug>', DetailedProfileView.as_view(), name='user-profile'),
    path('profile/<slug>/update/', ProfileUpdateView.as_view(), name='user-profile-update'),
]