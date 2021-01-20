from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Like, Comment, PostView
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# Create your views here.


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by('-published_date')
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    