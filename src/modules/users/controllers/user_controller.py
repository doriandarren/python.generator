from src.core.db.session import SessionLocal
from src.modules.users.repositories.user_repository import UserRepository
from src.modules.users.services.user_service import UserService


def register_user(name: str, email: str):
    db = SessionLocal()
    try:
        repo = UserRepository(db)
        service = UserService(repo)
        return service.register(name, email)
    finally:
        db.close()
        
        
## python -m src.modules.users.controllers.user_controller

if __name__ == "__main__":
    register_user("Dorian", "dorian@me.com")