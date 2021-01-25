from rest_framework import serializers
from .models import Post, Comment
from django.db.models import Q


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'detail_comment_url' ]
        lookup_field = 'slug'
    def get_user(self, obj):
        return obj.user.username
    def get_post(self, obj):
        return obj.post.title
    detail_comment_url = serializers.HyperlinkedIdentityField(
        view_name='comment-detail',
        lookup_field='id')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category',
                  'image', 'excerpt', 'author', 'published',
                  'content', 'date_created', 'detail_url',
                  'comment_url', 'update_url', 'delete_url',
                  'like_url'
                   ]
        lookup_field = 'slug'
    def get_author(self, obj):
        return obj.author.username
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detailed-post',
        lookup_field='slug'
    )
    comment_url = serializers.HyperlinkedIdentityField(
        view_name='comment',
        lookup_field='slug'
    )
    update_url = serializers.HyperlinkedIdentityField(
        view_name='update',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='delete',
        lookup_field='slug'
    )
    like_url = serializers.HyperlinkedIdentityField(
        view_name='like',
        lookup_field='slug'
    )
    
        
class PostDetailSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField(read_only=True)
    author = serializers.SerializerMethodField()
    comments  = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category',
                  'image', 'excerpt', 'author', 'published',
                  'content', 'date_created', 'comments',
                  'comment_count', 'view_count', 'like_count', 
                  'liked', 'owner', 'comment_url', 'update_url', 'delete_url',
                  'like_url' ]
        lookup_field = 'slug'
        
    def get_author(self, obj):
        return obj.author.username
    
    def get_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Post.objects.filter(Q(like__user=request.user) & Q(like__post=obj)).exists():
                return True
            return False
        
    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False
    comment_url = serializers.HyperlinkedIdentityField(
        view_name='comment',
        lookup_field='slug'
    )
    update_url = serializers.HyperlinkedIdentityField(
        view_name='update',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='delete',
        lookup_field='slug'
    )
    like_url = serializers.HyperlinkedIdentityField(
        view_name='like',
        lookup_field='slug'
    )
        
        
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title',  'category',
                  'image', 'excerpt', 'author', 'published',
                  'content', 'date_created']
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['like_count']
        
class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_delete_url','user', 'time_stamp', 'content', 'post']
        lookup_field = 'id'
    comment_delete_url = serializers.HyperlinkedIdentityField(
        view_name='comment-delete',
        lookup_field='id'
    )
        
    
        