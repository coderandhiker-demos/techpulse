from sqlalchemy import create_engine
from crawler_app import CrawlerApp
import logging
import os
from dotenv import load_dotenv

# load my environment vars
load_dotenv()
db_connection_string = os.environ.get("DB_CONNECTION_STRING")

# creating a long lived connection factory, this houses connection pool
engine = create_engine(db_connection_string)

# set up a basic terminal output logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def main():

    app = CrawlerApp(engine)
    app.run()
    app.get_articles()

if __name__ == '__main__':
    main()