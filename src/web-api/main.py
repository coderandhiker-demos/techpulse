import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from flask import Flask
from services import RssService

load_dotenv()
db_connection_string = os.environ.get("DB_CONNECTION_STRING")

engine = create_engine(db_connection_string)

# set up a basic terminal output logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)

services = []
services.append(RssService(engine, '/rss'))

for service in services:
    app.register_blueprint(service.blueprint, url_prefix=service.url_prefix)

if __name__ == '__main__':
    app.run()