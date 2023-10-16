from sqlalchemy import create_engine
from crawler_app import CrawlerApp

# Create a long-lived connection factory. Engine houses the connection pool
engine = create_engine('postgresql://postgres@localhost:5432/techpulse')

# Create any other dependencies that should be injected here

# Main app 
def main():

    # Inject dependencies here
    app = CrawlerApp(engine)
    app.run()

if __name__ == '__main__':
    main()