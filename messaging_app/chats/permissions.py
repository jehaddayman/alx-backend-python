from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    """
    يسمح فقط للمستخدمين المصادق عليهم واللي هم مشاركين في المحادثة بالوصول.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # تأكد أن المستخدم مشارك في المحادثة
        return request.user == obj.sender or request.user in obj.conversation.participants.all()
