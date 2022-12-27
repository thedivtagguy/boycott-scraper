import sys
sys.path.append('scraper')


from clean_twitter import clean_tweet
from clean_data import clean_text
from get_dates import get_dates
from fetch_tweets import get_tweets
from validate_config import validate_config
from parse_cli import parse_cli
from book_keeper import logging as log_details

import os
import json
import datetime
import crayons
import pandas as pd


# Read in config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Parse CLI arguments
config = parse_cli(config)
start_date, end_date = "", ""
week, year = datetime.datetime.now().isocalendar()[1], datetime.datetime.now().strftime('%Y')
df = pd.DataFrame()


# Validate config.json and exit if there are any errors
if validate_config(config) != True:
    print(crayons.red(f'❌ {validate_config(config)}'))
    print(crayons.red(f'Please fix the errors in config.json and try again.'))
    sys.exit()

# Fetch for current week if config['weekly'] is true
if config['scrape_type'] == 'weekly':
    start_date, end_date = get_dates(current_week=True)
    # Get tweets for current week
    print(crayons.blue(f' ℹ️ Current week: {week}, year: {year}'))
    df = get_tweets(from_date=start_date, to_date=end_date, config=config)

elif config['scrape_type'] == 'fullYear':
    # Get tweets for current year
    print(crayons.blue(f' ℹ️ Current year: {year}'))
    df = get_tweets(from_date=f'{config["year"]}-01-01', to_date=f'{config["year"]}-12-31', config=config)

elif config['scrape_type'] == 'custom':
    # Get tweets for custom date range
    print(crayons.blue(f' ℹ️ Custom date range: {config["start_date"]} - {config["end_date"]}'))
    df = get_tweets(from_date=config['start_date'], to_date=config['end_date'], config=config)

# Clean twitter data
if config['twitterExtract'] != 'false':
    print(crayons.yellow(f'📇 Extracting twitter data...'))
    df = clean_tweet(df)
else:
    print(crayons.red(f'📇 Not extracting twitter data...'))

if config['clean'] != 'false':
    # Clean text in the rawContent column
    print(crayons.yellow(f'🧹 Cleaning text...'))
    df['rawContent'] = df['rawContent'].apply(clean_text)
else: 
    print(crayons.red(f'🧹 Not cleaning text...'))

dates = {
    'start_date': start_date,
    'end_date': end_date
}

# Log details
log_details(config = config, length = len(df), dates = dates)

# Write CSV File to a new folder in data called current_week
if not os.path.exists('data/current_week'):
    os.makedirs('data/current_week')
df.to_csv(f'data/current_week/data.csv', index=False)
print(crayons.green(
    f'💾 Updated data to data/current_week/data.csv'))

