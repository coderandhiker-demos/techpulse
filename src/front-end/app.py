from flask import Flask, render_template, request, redirect, url_for
from blueprints import ArticlesBlueprint
from services import ArticleService
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# load configuration values and create db connection factory
load_dotenv()
db_connection_string = os.environ.get("DB_CONNECTION_STRING")
engine = create_engine(db_connection_string)

# create data services
article_service = ArticleService(engine)

# create flask app and wire up blueprints/routes
app = Flask(__name__)
blueprints = []
blueprints.append(ArticlesBlueprint(article_service, '/articles'))

for item in blueprints:
    app.register_blueprint(item.blueprint, url_prefix=item.url_prefix)

@app.route('/')
def index():
    return redirect(url_for('articles.get_articles'))

@app.route('/feeds')
def feeds_page():
    pass
    #feed_data = feeds.get_feeds()
    #return render_template('feeds/feeds.html', feed_data=feed_data)

if __name__ == '__main__':
    app.run(debug=True)
