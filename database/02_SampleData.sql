-- Insert a Single User (idempotent)
INSERT INTO users (user_id, username, email, display_name)
VALUES (1, 'Demo User', 'demouser@example.com', 'Demo User')
ON CONFLICT (user_id) DO NOTHING;

-- Insert RSS Feeds for Tech Websites (idempotent)
INSERT INTO rss_feeds (url, name, user_id) VALUES
    ('https://arstechnica.com/rss-feeds/', 'Ars Technica', 1),
    ('https://feeds.feedburner.com/techcrunch/', 'TechCrunch', 1),
    ('https://feeds.feedburner.com/TechRepublic_Blogs', 'TechRepublic', 1),
    ('https://www.zdnet.com/news/rss.xml', 'ZDNet', 1),
    ('https://feeds.feedburner.com/oreilly/radar/atom', 'O''Reilly Radar', 1),
    ('https://feeds.microsoft.com/AzureAppService', 'Microsoft Azure Blog', 1),
    ('https://news.microsoft.com/feed/', 'Microsoft News', 1),
    ('https://www.linux.com/feeds/latest', 'Linux.com', 1),
    ('https://planetpython.org/rss20.xml', 'Planet Python', 1),
    ('https://rss.app/', 'RSS.App', 1)
ON CONFLICT (url) DO NOTHING;
