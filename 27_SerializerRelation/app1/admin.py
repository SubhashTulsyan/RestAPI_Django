from django.contrib import admin
from .models import Player, Role
# Register your models here.
@admin.register(Player)
class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'team']
@admin.register(Role)
class RoleModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'player']