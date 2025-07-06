from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__username']

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants', [])
        if not participants or len(participants) < 2:
            return Response({'error': 'At least two participants required.'}, status=status.HTTP_400_BAD_REQUEST)
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        conversation.save()
        return Response(ConversationSerializer(conversation).data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        return Message.objects.filter(
            Q(sender=self.request.user) |
            Q(conversation__participants=self.request.user)
        ).distinct()

    def create(self, request, *args, **kwargs):
        sender = request.user
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')

        conversation = get_object_or_404(Conversation, pk=conversation_id)

        if sender not in conversation.participants.all():
            return Response(
                {'error': 'You are not a participant in this conversation.'},
                status=status.HTTP_403_FORBIDDEN
            )

        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )

        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)
    

    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 