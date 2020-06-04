from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'user_profile_app'

    def ready(self):
        from . signals import create_user_profile
