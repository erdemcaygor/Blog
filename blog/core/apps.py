
from django.apps import AppConfig


class CoreAppConfig(AppConfig):

    name = 'core'

    def ready(self):
        from core import signals
