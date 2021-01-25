from django.shortcuts import render, get_object_or_404
from rest_framework.generics import  ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Post, Like, Comment, PostView
from .serializers import PostSerializer, PostDetailSerializer, PostCreateUpdateSerializer, CommentCreateSerializer, LikeCreateSerializer, CommentSerializer, CommentDetailSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import MyPagination
from .permissions import IsOwner, IsCommentOwner
# Create your views here.


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by('-date_created').filter(published=True)
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

class UserPostListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = MyPagination
    
    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        return queryset

    
class PostDetailView(RetrieveAPIView):
    queryset =  Post.objects.order_by('-date_created')
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    
class PostCategoryView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = Post.objects.filter(category__iexact=category)
        return queryset


    
class PostCreateApi(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class PostUpdateApi(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        
class PostDeleteApi(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    
class CommentCreateApi(APIView):
    permission_class = [IsAuthenticated]
    serializer_class = CommentCreateSerializer
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)

        
class LikeCreateApi(APIView):
    permission_class = [IsAuthenticated]
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=post)
        data = {
            "messages": 'like'
        }
        return Response(data)
    
class CommentDetailApi(RetrieveAPIView):
    permission_class = [IsAuthenticated, IsOwner]
    queryset =  Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'
    
class CommentDeleteApi(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsCommentOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'
    
    
