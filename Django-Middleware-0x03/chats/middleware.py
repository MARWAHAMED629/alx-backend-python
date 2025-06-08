import os
from datetime import datetime
import logging
from django.http import HttpResponseForbidden

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_path = os.path.join(BASE_DIR, 'requests.log')

logger = logging.getLogger('request_logger')
logger.propagate = False

handler = logging.FileHandler(log_path)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)

if logger.hasHandlers():
    logger.handlers.clear()

logger.addHandler(handler)
logger.setLevel(logging.INFO)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'AnonymousUser'
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        response = self.get_response(request)
        return response
