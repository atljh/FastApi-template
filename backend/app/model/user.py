from app.model.base_model import BaseModel
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List

class User(BaseModel, table=True):
    email: str = Field(unique=True)
    password: str = Field()
    user_token: str = Field(unique=True)
    name: str = Field(default=None, nullable=True)


    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    referral_id: Optional[int] = Field(default=None, foreign_key="user.id")
    referral: Optional["User"] = Relationship(
        sa_relationship_kwargs={"remote_side": "User.id"}
    )
    referred_users: List["User"] = Relationship(
        back_populates="referral"
    )

