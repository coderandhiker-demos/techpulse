import feedparser

def parse_feed(url, show_content=False):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print("Title:", entry.title)
        print("Link:", entry.link)
        print("Published:", entry.published)
        
        if show_content:
            # Print the content if available
            if hasattr(entry, 'content'):
                print("Content:", entry.content[0].value)
            elif hasattr(entry, 'summary'):
                print("Content:", entry.summary)
            else:
                print("Content: Not available")
        
        print("------\n")

if __name__ == "__main__":
    #url = input("Enter the URL of the RSS Feed: ")
    url = 'http://feeds.arstechnica.com/arstechnica/index'
    parse_feed(url)
