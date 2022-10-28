"""
File in which we have the middleware for Django for Authenticating API requests
"""
import json
import logging
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpResponse
from ..helpers.create_response import create_response
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed, TokenBackendError, TokenError, exceptions
from django.contrib.auth import get_user_model
User = get_user_model()

# Initialize logger
logger = logging.getLogger(__name__)
# Get JWT secret key

SECRET_KEY = 'secret_or_key'


class CustomMiddleware(MiddlewareMixin):

    """
    Custom Middleware Class to process a request before it reached the endpoint
    """

    def process_request(self, request):
        """
        Custom middleware handler to check authentication for a user with JWT authentication
        :param request: Request header containing authorization tokens
        :type request: Django Request Object
        :return: HTTP Response if authorization fails, else None
        """

        routes_free = ['/auth/login/', '/auth/register/','/redoc/']

        if routes_free.__contains__(request.path):
            return None

        jwt_token = request.headers.get('authorization', None)
        logger.info(f"request received for endpoint {str(request.path)}")

        # If token Exists
        if jwt_token:
            try:
                auth = JWTAuthentication()
                tokenUser, token = auth.authenticate(request)
                if request.user.is_authenticated:
                    user = User.objects.get(id=token['user_id'])
                    if not user:
                        response, code = create_response(
                            401, {
                                "message": 'User not found'
                            }
                        )
                        return HttpResponse(json.dumps(response), status=code)
                    if tokenUser.email != user.email:
                        response, code = create_response(
                            401, {
                                "message": 'Access not match'
                            }
                        )
                        return HttpResponse(json.dumps(response), status=code)
                    if request.user.email != user.email:
                        response, code = create_response(
                            401, {
                                "message": 'Access not match'
                            }
                        )
                        return HttpResponse(json.dumps(response), status=code)
                    return None
            except (InvalidToken, AuthenticationFailed, TokenBackendError, TokenError, exceptions.ValidationError, exceptions.APIException, exceptions.PermissionDenied):
                response, code = create_response(
                    401, {"message": "Authorization has failed, Please send valid token."})
                logger.info(f"Response {response}")
                return HttpResponse(json.dumps(response), status=code)
            except Exception as e:
                response, code = create_response(
                    401, {
                        "message": e}
                )
            logger.info(f"Response {response}")
            return HttpResponse(json.dumps(response), status=code)

        else:
            response, code = create_response(
                401, {
                    "message": "Authorization not found, Please send valid token in headers"}
            )
            logger.info(f"Response {response}")
            return HttpResponse(json.dumps(response), status=code)
