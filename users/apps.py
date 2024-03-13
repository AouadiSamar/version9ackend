from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # Import signals here to avoid `AppRegistryNotReady` error
        import users.signals
