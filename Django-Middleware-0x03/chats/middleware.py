import logging
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
log_file = BASE_DIR / 'requests.log'

logger = logging.getLogger('request_logger')
handler = logging.FileHandler(log_file)
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
        response = self.get_response(request)
        return response