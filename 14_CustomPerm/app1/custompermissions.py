from rest_framework.permissions import BasePermission


class Customperm(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return False
    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)
        