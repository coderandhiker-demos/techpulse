from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class FeedFavorite(Base):
    __tablename__ = 'feed_favorites'

    favorite_id: Mapped[int] = mapped_column(primary_key=True, init=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    feed_id: Mapped[int] = mapped_column(ForeignKey('rss_feeds.feed_id'))
    favorite_date: Mapped[datetime] = mapped_column(init=False, server_default=func.now())