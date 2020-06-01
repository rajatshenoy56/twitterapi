from rest_framework.permissions import BasePermission

class IsUser(BasePermission):
    message = 'You are not the owner of the status'

    def has_object_permission(self,request,view,obj):
        return obj.user == request.user

class IsFollowerOrUser(BasePermission):
    def has_object_permission(self,request,view,obj):
        list1 = []
        b = request.user.follower.values()
        for i in b:
            list1.append(i['following_id'])

        if obj.user.id in list1 or obj.user == request.user:
            return True
        return False
		