from django.apps import AppConfig

app_name = 'app'

class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
