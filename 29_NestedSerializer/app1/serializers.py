from rest_framework import serializers
from .models import Player, Role
class RoleSer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'player']
class PlayerSer(serializers.ModelSerializer):
    roles = RoleSer(many = True)
    class Meta:
        model = Player
        fields = ['id', 'name', 'team', 'roles']

