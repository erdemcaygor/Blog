
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.contrib.sitemaps import ping_google
from .models import Post



@receiver(post_save, sender=Post)
def ping(sender, instance, **kwargs):

    if kwargs['created']:
        ping_google()