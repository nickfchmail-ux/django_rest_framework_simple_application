from rest_framework.permissions import BasePermission, SAFE_METHODS


class StaffOrBuyerAuthentication(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["GET", "POST"]:
            return True
        return request.user.is_staff
