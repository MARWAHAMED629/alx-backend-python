# messaging/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.recipient, message=instance)


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if not instance.pk:
        return  # جديد، لا تعديل

    old = Message.objects.get(pk=instance.pk)
    if old.content != instance.content:
        MessageHistory.objects.create(
            message=instance,
            old_content=old.content
        )
        instance.edited = True