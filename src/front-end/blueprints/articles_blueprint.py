from flask import render_template, request, Blueprint
from typing import LiteralString
from .base_blueprint import BaseBlueprint
from services import ArticleService


# wire up the article blueprint to keep all the article routes together
class ArticlesBlueprint(BaseBlueprint):
    def __init__(self, article_service:ArticleService, url_prefix:LiteralString):
        articles_blueprint = Blueprint('articles', __name__)
        super().__init__(articles_blueprint, url_prefix)
        self.article_service = article_service
        self.configure_services()

    # outer function as a method to gain access to self's state
    def configure_services(self):
        # inner functions for routes

        @self.blueprint.route('/')
        def get_articles():
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', type=int)

            if not per_page:
                per_page = 10  # Default to 10 if per_page is None

            articles, total_articles = self.article_service.get_articles(page, per_page)
            total_pages = (total_articles + per_page - 1) // per_page

            if articles:
                return render_template('articles/articles.html', articles=articles, page=page, per_page=per_page, total_pages=total_pages)
            else:
                return "Failed to fetch article data", 500

            
        # get a single article and render the viewer page
        @self.blueprint.route('/<int:id>')
        def get_article(id):
            article = self.article_service.get_article(id)
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)
            return render_template('articles/article.html', article=article, page=page, per_page=per_page)