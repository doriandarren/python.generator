from src.modules.users.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, name: str, email: str):
        # regla de negocio: email único
        if self.repo.get_by_email(email):
            raise ValueError("El email ya existe")

        # aquí podrías normalizar email, validar formato, etc.
        return self.repo.create(name=name, email=email)

    def get_profile(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        return user