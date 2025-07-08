from django.apps import AppConfig

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'  # Your app's name

    def ready(self):
        import courses.signals  # Make sure this points to the 'signals.py' file in the same app
