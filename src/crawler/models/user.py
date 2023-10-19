import uuid

from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str]
    aad_object_id: Mapped[uuid.UUID]
    date_added: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    email: Mapped[str]
    display_name: Mapped[str]
