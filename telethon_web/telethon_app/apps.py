from django.apps import AppConfig


class TelethonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telethon_app'

    def ready(self):
        import telethon_app.init
        return super().ready()