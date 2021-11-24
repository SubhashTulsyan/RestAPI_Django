from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender = User)
def cr_token_afterReg(sender, instance = None, created = False, **kwargs):
    print('kwargs: ', kwargs)
    if created:
        Token.objects.create(user = instance)
