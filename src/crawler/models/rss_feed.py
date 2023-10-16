from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class RssFeed(Base):
    __tablename__ = 'rss_feeds'

    feed_id: Mapped[int] = mapped_column(primary_key=True, init=False)
    url: Mapped[str]
    name: Mapped[str]
    date_added: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))