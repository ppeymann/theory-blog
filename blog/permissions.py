from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Only author can edit or delete the post.
    Others can only read.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
