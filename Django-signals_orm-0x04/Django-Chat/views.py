from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from rest_framework import viewsets, permissions

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)

    @action(detail=False, methods=['get'])
    def unread(self, request):
        """
        Custom endpoint: /messages/unread/
        Returns only unread messages for the logged-in user, optimized with .only()
        """
        user = request.user
        unread_messages = Message.unread.unread_for_user(user)
        serializer = self.get_serializer(unread_messages, many=True)
        return Response(serializer.data)
