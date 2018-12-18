from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS: DB의 변화가 없는 메소드
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
