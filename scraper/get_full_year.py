# This creates CSV files for the specified year

import pandas as pd
import os
# Get tweets function from get_tweets.py which is in scraper folder
import sys
sys.path.append('scraper')
from fetch_tweets import get_tweets

year = 2022

# Run it for the whole year
for week in range(1, 53):
    # Get tweets for current week
    df_twitter = get_tweets(year=year, weekNumber=week)

    # If data folder does not exist for the year, create it
    if not os.path.exists(f'data/{year}'):
        os.makedirs(f'data/{year}')

    # Write CSV File
    # Name of file is current year and week number
    df_twitter.to_csv(f'data/{year}/tweets-{year}-{week}.csv', index=False)

from_year = 2012
to_year = 2021

# Run it for all years from 2010 to 2021
for year in range(from_year, to_year + 1):
    for week in range(1, 53):
        # Get tweets for current week
        df_twitter = get_tweets(year=year, weekNumber=week)

        # If data folder does not exist for the year, create it
        if not os.path.exists(f'data/{year}'):
            os.makedirs(f'data/{year}')
        # Write CSV File
        df_twitter.to_csv(f'data/{year}/tweets-{year}-{week}.csv', index=False)