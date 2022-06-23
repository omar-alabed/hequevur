from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Permission to only allow access for admins.
    Assumes the presence of header X-ADMIN = 1
    """

    def has_permission(self, request, view):
        return 'X-ADMIN' in request.headers and request.headers['X-ADMIN'] == '1'
