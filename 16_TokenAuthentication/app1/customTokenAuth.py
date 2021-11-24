from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# http post http://127.0.0.1:8000/getToken/ username='****' password='****'
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data = request.data, context = {'request': request})
        ser.is_valid(raise_exception=True)
        user = ser.validated_data['user']
        token, created = Token.objects.get_or_create(user = user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'IsCreated': created,
        })