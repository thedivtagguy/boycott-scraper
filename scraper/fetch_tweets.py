# Function to get tweets from a given date range
#
# Usage:
#   df_twitter = get_tweets(currentWeek = True)
#   df_twitter = get_tweets(year = 2021, weekNumber = 1)
#   df_twitter = get_tweets(from_date = '2021-01-01', to_date = '2021-01-31')
#
# Returns:
#   df_twitter: pandas.DataFrame
#
# Raises:
#   ValueError: If invalid combination of arguments is provided
#
# Notes:
#   - This function uses the sns_scraper package to scrape tweets

import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
from halo import Halo
import datetime
import crayons
from get_dates import get_dates




def get_tweets(currentWeek = False, year = None, weekNumber = None, from_date = None, to_date = None, config = None):
    loc = "{}, {}, {}km".format(config['coordinates']['long'], config['coordinates']['lat'], config['coordinates']['radius'])
    search_term = config['search_term']
    limit = config['limit']
    print(crayons.blue(f'📍 Coordinates: {loc}'))
    print(crayons.blue(f'🔎 Search term: {config["search_term"]}'))
    if weekNumber is None:
        # Get current week number and year
        weekNumber, year = datetime.datetime.now().isocalendar()[1], datetime.datetime.now().strftime('%Y')
        

    # Get dates
    start_date, end_date = get_dates(current_week = currentWeek, year = year, week_num = weekNumber, start_date = from_date, end_date = to_date)

    print(crayons.yellow(f'🧾 Getting tweets from {start_date} to {end_date}...'))


    # Try to get tweets
    # If there is an error, log it and return an empty dataframe but don't stop the program
    df_twitter = pd.DataFrame()

    with Halo(text=' Fetching tweets', text_color='grey', spinner='dots'):
        try:
            # Get tweets
            df_twitter = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
            '{} since:{} until:{} geocode:"{}"'.format(config['search_term'], start_date, end_date, loc)).get_items(), int(config['limit'])))[['user', 'date','rawContent']]
        except Exception as e:
            print(crayons.red(f'Error: {e}'))
            return df_twitter

        
  
    # Add columns to dataframe
    if not df_twitter.empty: 
        df_twitter['user_location'] =  df_twitter['user'].apply(lambda x: x['location'])
        df_twitter['user_location'] = df_twitter['user_location'].apply(lambda x: x.strip())
        # Remove non-ascii characters
        df_twitter['user_location'] = df_twitter['user_location'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))



        df_twitter['verified'] =  df_twitter['user'].apply(lambda x: x['verified'])
        df_twitter['followers'] =  df_twitter['user'].apply(lambda x: x['followersCount'])
        df_twitter['created'] =  df_twitter['user'].apply(lambda x: x['created'])


    

    print(crayons.green(f'✅ Fetched {year}/week-{weekNumber} tweets'))

    return df_twitter
