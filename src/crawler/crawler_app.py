from sqlalchemy import Engine, insert, select
from sqlalchemy.orm import Session
from models import Article, RssFeed
from parsers import parse_feed
import logging

class CrawlerApp():
    def __init__(self, engine:Engine):
        self.engine = engine
        self.logger = logging.getLogger(__name__)

    def run(self):
        with Session(self.engine) as session:

            # 1. get the list of rss feeds from our database that we want to crawl
            feeds = session.execute(select(RssFeed))

            # 2. iterate through them and get data
            for (feed,) in feeds:
                articles = parse_feed(feed.url, feed.feed_id)

                self.logger.info(f'{feed.url}: {len(articles)}')

                if len(articles) > 0:
                    session.add_all(articles)

            # 3. save the session
            session.commit()

    def get_articles(self):
        with Session(self.engine) as session:
            
            # get all saved articles and print them to the terminal
            articles = session.execute(select(Article))
            for (article,) in articles:
                print(article)
