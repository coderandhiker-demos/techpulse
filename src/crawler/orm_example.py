from datetime import datetime
from typing import Optional
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass

class Base(MappedAsDataclass, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )


from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)

with engine.begin() as conn:
    Base.metadata.create_all(conn)


# when we have stateful instances of user, we want to persist the state
chris = User("Chris", "Chris Roberts")
print(chris)

# in the ORM we use Session. Session is to the ORM what Connection is to Core, the "thing that interacts with the transaction"

# as connection comes from the engine factory, Session comes from the sessionmaker factory
from sqlalchemy.orm import sessionmaker

# engine is usually a global variable - a module-level variable that is long lived
# the engine should be singular and reused, as should the session_factory
# don't make a new engine or session factory for every call
session_factory = sessionmaker(bind=engine)

# use the factory to create a session object
session = session_factory()

# you can use Core statements with it too
from sqlalchemy import text

# pass through down to the connection object and get a result... 
result = session.execute(text("select 'hello, world!' as message"))
print(result.first().message)

# we want to use a context manager for this too
from sqlalchemy import select
with session_factory() as sess:
    print(sess.execute(select(User.id)).all())

# you should use context manager patterns to manage Session scope
# however, we're going to use a single session and leave it open so you can see the interactions

session.add(chris)

# this is now pending
print(session.new)

# this will write when the flush happens and the unit of work is executed
select_statement = select(User).where(User.name == 'Chris')
result = session.execute(select_statement)
for row in result:
    print(row[0])

# the identity map is a weak mapping of objects keyed to their class/primary key identity
# so the same object in python was updated when the primary key and created_at were set
print(chris)

# this is the key: (<class '__main__.User'>, (1,), None)
print(dict(session.identity_map))

# that got us a consistent result back as a tuple, but when using the ORM we get objects using .scalars():

chris_too = session.scalars(select(User).where(User.name == "Chris")).first()
print(chris_too)

