from rest_framework import permissions

class CanCreatePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("setup.create_post")
    

class CanViewPostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("setup.view_post")
    
class CanUpdatePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("setup.change_post")
    
class CanDeletePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("setup.delete_post")