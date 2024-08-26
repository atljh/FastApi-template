from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.utils.schema import AllOptional


class BaseUser(BaseModel):
    email: str
    user_token: str
    name: str
    is_active: bool
    is_superuser: bool

    referral_id: Optional[int]

    class Config:
        orm_mode = True


class BaseUserWithPassword(BaseUser):
    password: str


class User(ModelBaseInfo, BaseUser, metaclass=AllOptional): ...


class FindUser(FindBase, BaseUser, metaclass=AllOptional):
    email__eq: str
    ...


class UpsertUser(BaseUser, metaclass=AllOptional):
    email: Optional[str]
    user_token: Optional[str]
    name: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    password: Optional[str]
    referral_id: Optional[int]

    class Config:
        orm_mode = True


class FindUserResult(BaseModel):
    founds: Optional[List[User]]
    search_options: Optional[SearchOptions]
