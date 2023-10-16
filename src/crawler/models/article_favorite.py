from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class ArticleFavorite(Base):
    __tablename__ = 'article_favorites'

    favorite_id: Mapped[int] = mapped_column(primary_key=True, init=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    entry_id: Mapped[int] = mapped_column(ForeignKey('articles.entry_id'))
    favorite_date: Mapped[datetime] = mapped_column(init=False, server_default=func.now())