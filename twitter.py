import requests
from twitter.scraper import Scraper
from twitter.util import find_key

def main(ids):
    # Initialize Scraper
    email = 'hyhgoodboy@outlook.com'
    username = '@hyhgoodboy233'
    password = 'h13117855518'
    scraper = Scraper(email, username, password)

    # Fetch tweets JSON data
    tweets_json = scraper.tweets(ids, limit=1)
    # Parse JSON
    tweet_data = []
    for d in tweets_json:
        instructions = find_key(d, 'instructions').pop()
        entries = find_key(instructions, 'entries').pop()
        for entry in entries:
            legacy = find_key(entry, 'legacy')
            for tweet in legacy:
                # For each tweet, check and extract media info separately
                media_info = {
                    'media_url_https': None,
                    'media_type': None
                }
                if 'extended_entities' in tweet:
                    media_list = tweet['extended_entities'].get('media', [])
                    if media_list:
                        media_info['media_url_https'] = [media['media_url_https'] for media in media_list if 'media_url_https' in media]
                        media_info['media_type'] = [media['type'] for media in media_list if 'type' in media]
                # Add media info to tweet data
                tweet.update(media_info)
                tweet_data.append(tweet)
    return tweet_data
