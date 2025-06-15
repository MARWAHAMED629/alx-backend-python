# messaging/admin.py
from django.contrib import admin
from .models import Message, Notification, MessageHistory

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'timestamp', 'read', 'edited')
    list_filter = ('sender', 'recipient', 'timestamp', 'read', 'edited')
    search_fields = ('sender__username', 'recipient__username', 'content')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'read', 'timestamp')
    list_filter = ('read', 'timestamp')
    search_fields = ('user__username', 'message__content')

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'timestamp')
    search_fields = ('message__content', 'old_content')