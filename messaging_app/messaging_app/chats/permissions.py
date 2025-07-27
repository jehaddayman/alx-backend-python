from rest_framework.permissions import BasePermission

class IsParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        # تحقق إن المستخدم هو أحد المشاركين بالمحادثة
        return request.user in obj.participants.all()

class IsOwnerOfMessage(BasePermission):
    def has_object_permission(self, request, view, obj):
        # تحقق إن المستخدم هو مرسل الرسالة
        return obj.sender == request.user
