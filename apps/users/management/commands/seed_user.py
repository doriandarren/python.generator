import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

load_dotenv()


class Command(BaseCommand):
    help = "Crea o actualiza usuarios por defecto"

    def handle(self, *args, **kwargs):
        
        
        password = os.getenv("SEED_USER_PASSWORD")

        if not password:
            raise CommandError(
                "La variable SEED_USER_PASSWORD no está configurada."
            )
        
        self.create_user(
            username="admin",
            email="admin@splytin.com",
            password=password,
            is_staff=True,
            is_superuser=True,
        )

        self.create_user(
            username="manager",
            email="manager@splytin.com",
            password=password,
            is_staff=True,
            is_superuser=False,
        )

        self.create_user(
            username="user",
            email="user@splytin.com",
            password=password,
            is_staff=True,
            is_superuser=False,
        )
        
        
    

    def create_user(self, username, email, password, is_staff=False, is_superuser=False):
        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )

        user.email = email
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Usuario creado: {user.username}"))
        else:
            self.stdout.write(self.style.WARNING(f"Usuario actualizado: {user.username}"))

        return user