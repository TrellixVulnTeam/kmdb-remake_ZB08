from rest_framework.permissions import BasePermission
import ipdb

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff == True and request.user.is_superuser == True

class CriticPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff == True and request.user.is_superuser == False
           

class IsAdminCriticOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_staff == True or request.user.is_superuser == True