# from rest_framework.views import exception_handler

# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)

#     if response is not None and response.status_code == 401:  # Unauthenticated
#         response.data['message'] = "You need to log in to access this resource."
#         # response.data['login_url'] = "https://repair-or-replace-back-end.onrender.com/api/login/"
#         response.data['login_url'] = "http://127.0.0.1:8000/api/login/"
#     return response

import logging
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    logger.error(f"Custom Exception Handler Triggered: {exc}")

    response = exception_handler(exc, context)

    if response is not None and response.status_code == 401:  # Unauthenticated
        response.data['message'] = "You need to log in to access this resource."
        response.data['login_url'] = "http://127.0.0.1:8000/api/login/"

    return response
