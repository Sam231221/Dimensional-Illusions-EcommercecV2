from django.apps import AppConfig


class EhubConfig(AppConfig):
    name = 'EHub'
  
    def ready(self):
        import EHub.signals