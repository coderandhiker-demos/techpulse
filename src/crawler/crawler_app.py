from sqlalchemy import Engine, insert, select
from sqlalchemy.orm import Session
from models import Article, RssFeed
from parsers import parse_feed

class CrawlerApp():
    def __init__(self, engine:Engine):
        self.engine = engine

    def run(self):
        with Session(self.engine) as session:

            # 1. get the list of RSS feeds to crawl
            feeds = session.execute(select(RssFeed))
        
            # 2. iterate through them fetching data (use tuple unpacking)
            for (feed,) in feeds:                
                articles = parse_feed(feed.url, feed.feed_id)

                if len(articles) > 0:
                    session.add_all(articles)

            # 3. save the session     
            session.commit()
