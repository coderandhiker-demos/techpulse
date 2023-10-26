from flask import Blueprint, jsonify
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from typing import LiteralString
from .base_service import BaseService
from models import RssFeed

class RssService(BaseService):
    def __init__(self, engine: Engine, url_prefix: LiteralString):
        rss_blueprint = Blueprint('rss', __name__)
        super().__init__(engine, rss_blueprint, url_prefix)
        self.configure_routes()

    def configure_routes(self):
        @self.blueprint.route('/feeds')
        def get_feeds():
            with Session(bind=self.engine) as session:
                result = session.execute(select(RssFeed))
                feeds = [row[0] for row in result]
                return jsonify(feeds)
                
        @self.blueprint.route('/feed/<int:id>')
        def get_feed_by_id(id):
            with Session(bind=self.engine) as session:
                feed = session.execute(
                    select(RssFeed).where(RssFeed.feed_id == id)
                ).first()[0]
                if feed:
                    return jsonify(feed)
                else:
                    return f'Feed {id} not found', 404