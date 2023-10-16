from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Article(Base):
    __tablename__ = 'articles'

    entry_id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    link: Mapped[str]
    published: Mapped[datetime]
    content: Mapped[str]
    feed_id: Mapped[int] = mapped_column(ForeignKey('rss_feeds.feed_id'))