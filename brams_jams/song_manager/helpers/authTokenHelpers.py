import re
import jwt
from django.conf import settings

class AuthTokenHelpers:
    @staticmethod
    def get_user_from_token(request=None):
        pass
        try:
            cookies = request.META['HTTP_COOKIE']
            token_groups = re.match('jwt_access=(.*?)\s', cookies)
            token = token_groups.group(1)
            jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except Exception as e:
            print("this is the exception ", e)