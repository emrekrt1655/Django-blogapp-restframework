from django.urls import path
from .views import PostListView, PostDetailView, PostPublishedView, PostCategoryView

urlpatterns = [
    path('', PostListView.as_view()),
    path('published/', PostPublishedView.as_view()),
    path('category/', PostCategoryView.as_view()),
    path('<slug>/', PostDetailView.as_view()),
]