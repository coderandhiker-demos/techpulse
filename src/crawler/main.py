from sqlalchemy import create_engine
from crawler_app import CrawlerApp

# creating a long lived connection factory, this houses connection pool
engine = create_engine('postgresql://postgres@localhost:5432/techpulse')

def main():

    app = CrawlerApp(engine)
    app.run()
    app.get_articles()

if __name__ == '__main__':
    main()