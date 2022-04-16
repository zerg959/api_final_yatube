from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return (
    #         request.method in permissions.SAFE_METHODS
    #         or request.user.is_authenticated
    #     )
    #
    # def has_object_permission(self, request, view, obj):
    #     return obj.author == request.user
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True
