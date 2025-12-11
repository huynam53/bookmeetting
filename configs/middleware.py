import os

import jwt
from django.http import HttpResponse

from app.core import UserInfo


def get_anonymous() -> UserInfo:
    user_info = UserInfo(email="anonymous@anonymous.com")
    return user_info


class UserInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_path = request.get_full_path()
        if url_path.startswith("/api/v1/public"):
            # by pass verify token
            request.user_info = get_anonymous()
        else:
            auth_header = request.META.get('HTTP_AUTHORIZATION')
            claims = self.get_token_claims(auth_header)
            if isinstance(claims, HttpResponse):
                return claims

            request.user_info = UserInfo(
                id=claims.get('sub'),
                username=claims.get('username'),
                email=claims.get('email'),
                firstname=claims.get('firstname'),
                lastname=claims.get('lastname'),
                avatar=claims.get('avatar'),
            )
        response = self.get_response(request)
        return response

    @classmethod
    def get_token_claims(cls, auth_header: str):
        if auth_header is not None:
            arr = auth_header.split(" ")
            token = None
            if len(arr) == 2:
                token = arr[1]
            if token is not None:
                try:
                    claims = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=["HS256"])
                    return claims
                except Exception as e:
                    return HttpResponse("Invalid Token!", status=401)
            else:
                return HttpResponse("Token is missing!", status=401)
        else:
            return HttpResponse("Token is missing!", status=401)
