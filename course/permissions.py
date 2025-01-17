from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_staff and request.method == 'DELETE':
            return True
        return False


class CoursePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.method in SAFE_METHODS
