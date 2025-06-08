from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsParticipantOfConversation(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user in obj.conversation.participants.all()