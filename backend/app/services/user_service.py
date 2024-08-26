from passlib.context import CryptContext
from app.repository.user_repository import UserRepository
from app.services.base_service import BaseService
from app.model.user import User 
from app.schema.user_schema import UpsertUser 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    def add_user(self, user_data: UpsertUser) -> User:
        # Assuming password hashing is done here
        new_user = User(**user_data.dict())
        return self.user_repository.create(new_user)

