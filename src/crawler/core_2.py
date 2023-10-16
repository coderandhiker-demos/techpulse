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
    
        # init=False means don't include in the default constructor in the python dataclass
        # server side timestamp

from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)

with engine.begin() as conn:
    Base.metadata.create_all(conn)


from sqlalchemy import insert
insert_statement = insert(User).values(name="Chris", fullname="Chris Roberts")
print(insert_statement)

compiled = insert_statement.compile()
print (compiled.params)

with engine.connect() as conn:
    result = conn.execute(insert_statement)
    print(f'Inserted 1 row, new id: {result.inserted_primary_key}')
    conn.commit()


# when using SQLAlchemy Core
with engine.begin() as conn:
    result = conn.execute(
        insert(User), 
        [
            {'name': 'John', 'fullname': 'John Doe'},
            {'name': 'Jane', 'fullname': 'Jane Smith'}
        ])

from sqlalchemy import text

query_text = text("select * from user_account")

with engine.connect() as conn:
    results = conn.execute(query_text)
    for row in results:
        print(row)
    
with engine.connect() as conn:
    for row in conn.execute(query_text):
        print(row.name)

# now, lets look at the SQLAlchemy Core expression language
from sqlalchemy import select 
stmt = select(User.name)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row.name)

# lets see what queries we can generate using SQLAlchemy Core:
#print(select(User))

# add in a second class
from sqlalchemy import ForeignKey
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

with engine.begin() as conn:
    Base.metadata.create_all(conn)
    conn.execute(
        insert(Address), 
        [
            {'email_address': 'chrisrt@microsoft.com', 'user_id': 1},
            {'email_address': 'coderandhiker@frostfireai.onmicrosoft.com', 'user_id': 1},
            {'email_address': 'johndoe@example.com', 'user_id': 2},
            {'email_address': 'janesmith@example.com', 'user_id': 3}
        ])

# the default behavior puts the froms in with a comma... big cartesian product
#print(select(User.name, User.fullname, Address.email_address))

# so we can add a join using the select().join_from() method
# note the on clause was auto generated because we used ForeignKey
stmt = select(User.name, User.fullname, Address.email_address).join_from(User, Address)
print(stmt)

with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(f'{row.name:15} {row.fullname:25} {row.email_address}')

# find the users with multiple email addresses...
email_address_count = (
    select(Address.user_id, func.count(Address.email_address).label('email_count'))
        .group_by(Address.user_id)
        .having(func.count(Address.email_address) > 1).subquery()
)

# subquery_name.c => column attributes live here
stmt = select(User.name, email_address_count.c.email_count).join_from(User, email_address_count)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f'{row.name} has {row.email_count} email addresses')


# expressions with bound parameters...
print(User.name == 'Chris')

# case invariant contains
print(User.name.icontains('hri'))

# ok, on to the more common stuff - where method
stmt = select(User.name).where(User.name.in_(['Chris', 'Jane']))
print(stmt)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row.name)

# you can just add .order_by(User.id) etc.

# ORM is another way to talk to the database in terms of Python objects, their state and mutations on their state
# the ORM will generate the statements based on the object state


