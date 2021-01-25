from django.urls import path
from .views import *

urlpatterns = [
    path('postlist/', PostListView.as_view(), name= 'list'),
    path('userlist/', UserPostListView.as_view(), name= 'user-list'),
    path('create/', PostCreateApi.as_view(), name='create'),
    path('<category>/', PostCategoryView.as_view()),
    path('update/<slug>/', PostUpdateApi.as_view(), name= 'update'),
    path('delete/<slug>/', PostDeleteApi.as_view(), name= 'delete'),
    path('comment/<slug>/', CommentCreateApi.as_view(), name= 'comment'),
    path('commentdetail/<id>/', CommentDetailApi.as_view(), name= 'comment-detail'),
    path('commentdelete/<id>/', CommentDeleteApi.as_view(), name= 'comment-delete'),
    path('like/<slug>/', LikeCreateApi.as_view(), name= 'like'),
    path('<slug>/', PostDetailView.as_view(), name= 'detailed-post'),
]