from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

User = get_user_model()

@login_required
def delete_user(request):
    user = request.user
    if request.method == 'POST':
        user.delete()

        return redirect('login')
    else:
        return HttpResponseForbidden("You must submit a POST request to delete your account.")
