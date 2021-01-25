from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from blog import serializers
from rest_framework import status
from users.models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProfileSerializer, UserSerializer, ProfileUpdateSerializer, ProfileDetailSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class=ProfileSerializer

class DetailedProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class=ProfileDetailSerializer
    lookup_field = 'slug'
    
class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save()

