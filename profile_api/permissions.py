from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Alow user to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user tring to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id    