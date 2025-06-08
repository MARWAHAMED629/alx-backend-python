from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission class that allows access only to:
    
    - Authenticated users.
    - Participants of the conversation associated with the message object.
    """

    def has_permission(self, request, view):
        # Check that the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Grant access only if the user is a participant in the conversation
        return request.user in obj.conversation.participants.all()