from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
class CustomAuth(BaseAuthentication):
    def authenticate(self, request):
        user = request.GET.get('username')

        if user is None:
            return None
        try:
            userobj = User.objects.get(username = user)
        except User.DoesNotExist:
            raise AuthenticationFailed('User NOT Found')
        return (userobj, None)