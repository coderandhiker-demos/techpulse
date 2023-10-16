from sqlalchemy import Table, Column, MetaData
from sqlalchemy import DateTime, Integer, String

metadata = MetaData()

user_account_table = Table(
    "user_account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("fullname", String),
    Column("created_at", DateTime)
)

