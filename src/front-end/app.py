from flask import Flask, render_template, request
from services import ArticleService
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import requests
import json
from models import Pokemon

app = Flask(__name__)

load_dotenv()
db_connection_string = os.environ.get("DB_CONNECTION_STRING")

engine = create_engine(db_connection_string)

article_service = ArticleService(engine)


# the root page lists articles
@app.route('/')
def index():
        # Make a GET request to the ArticleService
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=20, type=int)

    articles = article_service.get_articles(page, per_page)

    if articles:
        return render_template('articles/articles.html', articles=articles)
    else:        
        return "Failed to fetch article data", 500

@app.route('/article/<int:id>')
def read_article(id):
    article = article_service.get_article(id)
    return render_template('articles/article.html', article=article)

@app.route('/test')
def test_method():   
    url = 'https://pokeapi.co/api/v2/pokemon/ditto'
    result = requests.get(url)
    content = result.content.decode('utf-8')
    # step 1 
    data_dictionary = json.loads(content)

    # step 2 create the object of a dataclass
    #pokemon = Pokemon(**data_dictionary)
    return render_template('pokemon/pokemon.html', item=data_dictionary)

@app.route('/feeds')
def feeds_page():
    pass
    #feed_data = feeds.get_feeds()
    #return render_template('feeds/feeds.html', feed_data=feed_data)

if __name__ == '__main__':
    app.run(debug=True)
