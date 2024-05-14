from django.apps import AppConfig


class RembourssementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rembourssement'





    def ready(self):
        
        
        import rembourssement.signals
