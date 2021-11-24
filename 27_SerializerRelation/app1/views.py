from rest_framework import viewsets
from .models import Player, Role
from .serializers import PlayerSer, RoleSer

class PlayerAPI(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    print('Player qs: ', queryset)
    serializer_class = PlayerSer

class RoleAPI(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    print('Role qs: ', queryset)
    serializer_class = RoleSer