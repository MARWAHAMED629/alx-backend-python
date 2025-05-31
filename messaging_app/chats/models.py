from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model extending Django's built-in AbstractUser.
    This allows future customization like adding fields such as avatar, bio, etc.
    """
    pass


class Conversation(models.Model):
    """
    Represents a conversation involving multiple users.
    """
    participants = models.ManyToManyField(User, related_name='conversations')  # Many-to-many relationship with users
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the conversation is created

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    """
    Represents a single message sent by a user within a conversation.
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')  # The user who sent the message
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')  # The conversation this message belongs to
    content = models.TextField()  # The text content of the message
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the date/time when the message is created

    def __str__(self):
        return f"Message from {self.sender.username} in Conversation {self.conversation.id}"
