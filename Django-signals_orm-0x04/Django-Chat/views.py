# Django-Chat/Views/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from django.db.models import Prefetch, Q
from .models import Message

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
    Use select_related and prefetch_related for query optimization.
    """
    user = request.user
    # Filter the message to only those where the user is sender or receiver
    message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver')
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
        )
        .filter(Q(sender=user) | Q(receiver=user)),
        pk=message_id
    )

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
    return render(request, 'messaging/conversation_detail.html', context)from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST


@require_POST
@login_required
def delete_user(request):
    request.user.delete()
    return redirect("home")