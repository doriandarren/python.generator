from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Crea un usuario por defecto"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = "dorian"
        email = "dorian@gmail.com"
        password = "123456"

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"El usuario '{username}' ya existe."))
            return

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(self.style.SUCCESS(f"Usuario creado correctamente: {user.username}"))