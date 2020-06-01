from rest_framework.permissions import BasePermission

class isLoggedIn(BasePermission):
    message = 'You are already logged in'

    def has_permission(self,request,view):
        if request.user.id:
            return False
        return True
