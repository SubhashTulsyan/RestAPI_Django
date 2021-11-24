from django.db import models
class Player(models.Model):
    name = models.CharField(max_length=80)
    team = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Role(models.Model):
    name = models.CharField(max_length=80)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='roles')
    def __str__(self):
        return self.name
    
