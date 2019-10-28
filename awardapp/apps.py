from django.apps import AppConfig


class AwardappConfig(AppConfig):
    name = 'awardapp'

    def ready(self):
       import awardapp.signals
