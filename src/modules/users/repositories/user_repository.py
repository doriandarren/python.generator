from sqlalchemy.orm import Session
from src.modules.users.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user