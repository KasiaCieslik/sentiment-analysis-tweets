from twython import Twython
import time
from .open_json import open_json_file


def scrap_tweet_from_twitter(query,language,creds_path, range_number,tweets_number_for_every_range):
    """
    Real time tweets scraping

    Parameters
    ----------
    query: str
    language: str
    creds_path: str
    range_number: int -number of for loops
    tweets_number_for_every_range: int -number of tweets which are scraped in every loop

    Returns
    -------
    List[dict]
    """
    creds = open_json_file(creds_path)
    tweets = []
    t = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], 
                        creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
    since_id = None
    for _ in range(range_number):
        search=t.search(q = query,lang = language,count=tweets_number_for_every_range,since_id=since_id)
        since_id = search['search_metadata']['max_id']
        tweets.extend(search['statuses'])
        print(since_id)
        time.sleep(30)
    return tweets

