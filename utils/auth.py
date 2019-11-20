from rest_framework.authentication import BaseAuthentication
from apps.users.models import UserToken
from rest_framework.exceptions import AuthenticationFailed


class MyToken(BaseAuthentication):

    def authenticate(self, request):
        token = request.query_params.get('token')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise AuthenticationFailed('认证失败')
        return token_obj.user,token_obj