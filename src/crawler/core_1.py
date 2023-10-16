from datetime import datetime
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column

class Base(MappedAsDataclass, DeclarativeBase):
    pass

# it is also a dataclass, it has methods like default __init__, __repr__ based on the directives
# passed to mapped_column
class User(Base):
    __tablename__ = "user_account"
    # mapped means it is mapped to the table column
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow)

# >>> User.__table__ was created and has all those things with MetaData and Column definitions

# add in a second class
from sqlalchemy import ForeignKey
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))


from sqlalchemy import create_engine

# .create_all will create everything on this connection
engine= create_engine("sqlite://", echo=True)
with engine.begin() as conn:
    Base.metadata.create_all(conn)



