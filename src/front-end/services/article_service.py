from flask import Blueprint, jsonify, request
from sqlalchemy import Engine, select, text
from sqlalchemy.orm import Session
from typing import LiteralString
from .base_service import BaseService
from models import Article


class ArticleService(BaseService):
    def __init__(self, engine):
        super().__init__(engine)

    def get_articles(self, page, per_page):        
        with Session(bind=self.engine) as session:
            total_articles = session.scalar(text('select count(*) from articles;'))                
            result = session.execute(select(Article).limit(per_page).offset((page - 1) * per_page))
            articles = [row[0].as_dict() for row in result]
            return articles
        
    def get_article(self, id):
        with Session(bind=self.engine) as session:
            article = session.execute(select(Article).where(Article.entry_id == id)).first()[0]
            return article