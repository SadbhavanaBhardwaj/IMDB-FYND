from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
        Allows access to admin only
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="ADMIN")
        