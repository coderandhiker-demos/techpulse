import feedparser
from typing import List
from models import Article

def parse_feed(url, feed_id) -> List[Article]:
    parsed_feed = feedparser.parse(url)
    articles = []
    print(f'Found {len(parsed_feed.entries)} articles for {url}')
    for entry in parsed_feed.entries:
        content = ''
        if hasattr(entry, 'content'):
            content = entry.content[0].value
        elif hasattr(entry, 'summary'):
            content = entry.summary
            
        article = Article(entry.title, entry.link, entry.published, content, feed_id)
        articles.append(article)

    return articles