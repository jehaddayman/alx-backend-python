from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Router الأساسي
router = NestedDefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# راوتر متداخل للرسائل داخل المحادثات
conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),
]
