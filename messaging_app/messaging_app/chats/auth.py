from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MessageSerializer, ConversationSerializer
from .models import Message, Conversation
from .permissions import IsOwnerOfMessage, IsParticipant

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipant]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfMessage]
