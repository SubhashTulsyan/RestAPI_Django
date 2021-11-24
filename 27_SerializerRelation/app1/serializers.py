from rest_framework import serializers
from .models import Player, Role
class PlayerSer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Player
        fields = ['id', 'name', 'team', 'role']
class RoleSer(serializers.ModelSerializer):
    player = serializers.StringRelatedField()
    class Meta:
        model = Role
        fields = ['id', 'name', 'player']
