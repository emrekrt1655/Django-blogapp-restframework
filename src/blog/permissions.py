from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "You have to be an owner of this post"
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsCommentOwner(BasePermission):
    message = "You have to be an owner of this comment"
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user