from rest_framework import viewsets
from .models import Player, Role
from .serializers import PlayerSer, RoleSer

class PlayerAPI(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSer

class RoleAPI(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSer