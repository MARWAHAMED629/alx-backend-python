from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from django.db.models import Prefetch, Q
from .models import Message
from django.views.decorators.cache import cache_page 
User = get_user_model()


@login_required
def delete_user(request):
    """
    Allow logged-in user to delete their account via POST request only.
    """
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')  # Redirect to login or homepage after deletion
    else:
        return HttpResponseForbidden("You must submit a POST request to delete your account.")


@login_required
def conversation_detail(request, message_id):
    """
    Display the details of a message and its threaded replies.
    Only allow access if the current user is either the sender or receiver of the message.
    Uses select_related and prefetch_related for query optimization.
    """
    user = request.user
    message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver')
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
        )
        .filter(Q(sender=user) | Q(receiver=user)),
        pk=message_id
    )

    # Mark the message as read if it's addressed to the current user
    if message.receiver == user and not message.read:
        message.read = True
        message.save(update_fields=['read'])

    def get_threaded_replies(message):
        """
        Recursively fetch all replies to a message in a threaded format.
        Uses select_related for performance.
        """
        replies = Message.objects.filter(parent_message=message).select_related('sender', 'receiver')
        return [{
            'message': reply,
            'replies': get_threaded_replies(reply)
        } for reply in replies]

    threaded_replies = get_threaded_replies(message)

    context = {
        'message': message,
        'threaded_replies': threaded_replies,
    }
    return render(request, 'messaging/conversation_detail.html', context)


@login_required
def unread_messages(request):
    """
    Display all unread messages for the logged-in user.
    Uses .only() to optimize the query.
    """
    user = request.user
    unread_messages = Message.unread.unread_for_user(user)
    context = {
        'unread_messages': unread_messages
    }
    return render(request, 'messaging/unread_messages.html', context)


@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')
    else:
        return HttpResponseForbidden("You must submit a POST request to delete your account.")


@cache_page(60)
@login_required
def conversation_detail(request, message_id):
    """
    Display the details of a message and its threaded replies.
    This view is cached for 60 seconds to improve performance.
    Note: Marking the message as read will not take effect immediately due to caching.
    """
    user = request.user
    message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver')
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
        )
        .filter(Q(sender=user) | Q(receiver=user)),
        pk=message_id
    )

    def get_threaded_replies(message):
        replies = Message.objects.filter(parent_message=message).select_related('sender', 'receiver')
        return [{
            'message': reply,
            'replies': get_threaded_replies(reply)
        } for reply in replies]

    threaded_replies = get_threaded_replies(message)

    context = {
        'message': message,
        'threaded_replies': threaded_replies,
    }
    return render(request, 'messaging/conversation_detail.html', context)