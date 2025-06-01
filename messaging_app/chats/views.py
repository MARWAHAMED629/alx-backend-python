from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.shortcuts import get_object_or_404

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
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        sender = request.user
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')

        conversation = get_object_or_404(Conversation, pk=conversation_id)
        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )
        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)