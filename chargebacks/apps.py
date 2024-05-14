from django.apps import AppConfig


class ChargebacksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chargebacks'

    def ready(self):
        
        
        
        import chargebacks.signals 
