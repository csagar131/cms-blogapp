from rest_framework import permissions



class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        print('getting here')
        print(request.user,obj.author)
        return request.user == obj.author