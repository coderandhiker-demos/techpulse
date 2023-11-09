from flask import Blueprint, jsonify, request
from sqlalchemy import Engine, select, text
from sqlalchemy.orm import Session
from typing import LiteralString
from .base_service import BaseService
from models import Article
import json


class ArticleService(BaseService):
    def __init__(self, engine: Engine, url_prefix: LiteralString):
        rss_blueprint = Blueprint("article", __name__)
        super().__init__(engine, rss_blueprint, url_prefix)
        self.configure_routes()

    def configure_routes(self):
        @self.blueprint.route("/list")
        def get_feeds():

            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=20, type=int)
            
            with Session(bind=self.engine) as session:
                total_articles = session.scalar(text('select count(*) from articles;'))                
                result = session.execute(select(Article).limit(per_page).offset((page - 1) * per_page))
                articles = [row[0].as_dict() for row in result]
                
                response = {
                    "page": page,
                    "per_page": per_page,
                    "total_articles": total_articles,
                    "data": json.dumps(articles, default=BaseService.serialize_datetime)
                }                
                return response, 200