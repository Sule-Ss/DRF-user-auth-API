from rest_framework import permissions


class KendiProfiliYadaReadOnly(permissions.BasePermission):
    #! models içindeki Profilin userını check edebilmek için object bazında bir izinleme olup olmadığını denetlemek lazım.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class DurumSahibiYadaReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profil == request.user.profil
