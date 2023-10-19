SET search_path = techpulse, public;

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    aad_object_id UUID, -- Store AAD Object ID for each user
    date_added TIMESTAMP DEFAULT NOW(),    
    email VARCHAR(255),
    display_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS  rss_feeds (
    feed_id SERIAL PRIMARY KEY,
    url TEXT NOT NULL UNIQUE,
    name VARCHAR(255),
    date_added TIMESTAMP DEFAULT NOW(),
    user_id INT REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS  articles (
    entry_id SERIAL PRIMARY KEY,
    title TEXT,
    link TEXT,
    published TIMESTAMP,
    content TEXT,
    feed_id INT REFERENCES rss_feeds(feed_id)
);

CREATE TABLE IF NOT EXISTS  feed_favorites (
    favorite_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    feed_id INT REFERENCES rss_feeds(feed_id),
    favorite_date TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS  article_favorites (
    favorite_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    entry_id INT REFERENCES articles(entry_id),
    favorite_date TIMESTAMP DEFAULT NOW()
);