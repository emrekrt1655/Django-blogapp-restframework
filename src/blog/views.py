from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Like, Comment, PostView
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
# Create your views here.


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by('-date_created')
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    
class PostDetailView(RetrieveAPIView):
    queryset =  Post.objects.order_by('-date_created')
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]

class PostPublishedView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().filter(published = True)
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    
class PostCategoryView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = Post.objects.order_by('-date_created').filter(category__iexact=category)
        
        serializer = PostSerializer(queryset, many=True)
        
        return Response(serializer.data)