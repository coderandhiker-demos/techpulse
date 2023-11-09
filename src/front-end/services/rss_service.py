from flask import Blueprint, jsonify
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from typing import LiteralString
from .base_service import BaseService
from models import RssFeed


class RssService(BaseService):
    def __init__(self, engine: Engine):
        super().__init__(engine)

    def get_feeds(self):
        with Session(bind=self.engine) as session:
            result = session.execute(select(RssFeed))
            feeds = [row[0] for row in result]
            return feeds

    def get_feed_by_id(self, id):
        with Session(bind=self.engine) as session:
            feed = session.execute(
                select(RssFeed).where(RssFeed.feed_id == id)
            ).first()[0]
            if feed:
                return feed
            else:
                raise f"Feed {id} not found"
