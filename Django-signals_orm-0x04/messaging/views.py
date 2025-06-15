from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from django.db.models import Prefetch
from .models import Message

User = get_user_model()

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')
    else:
        return HttpResponseForbidden("You must submit a POST request to delete your account.")

@login_required
def conversation_detail(request, message_id):
    message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver')
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
        ),
        pk=message_id
    )

    def get_threaded_replies(message):
        replies = message.replies.all()
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