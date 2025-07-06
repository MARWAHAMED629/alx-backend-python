from datetime import datetime, timedelta
import logging
from datetime import datetime

from django.http import HttpResponseForbidden

from django.conf import settings

logger = logging.getLogger('request_logger')
handler = logging.FileHandler(settings.LOG_FILE_PATH)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'AnonymousUser'
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_log = {}

    def __call__(self, request):
        ip = self.get_client_ip(request)
        now = datetime.now()

        if request.method == 'POST':
            timestamps = self.message_log.get(ip, [])
            timestamps = [ts for ts in timestamps if now - ts < timedelta(minutes=1)]
            if len(timestamps) >= 5:
                return HttpResponseForbidden("Rate limit exceeded: Max 5 messages per minute.")
            timestamps.append(now)
            self.message_log[ip] = timestamps

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if not (18 <= current_hour < 21):
            return HttpResponseForbidden("Access to chat is only allowed between 6 PM and 9 PM.")
        return self.get_response(request)
    
class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user_role = getattr(request.user, 'role', None)
            if user_role not in ['admin', 'moderator']:
                return HttpResponseForbidden("Access denied: Admin or Moderator role required.")
        return self.get_response(request)
