from clean_twitter import clean_tweet
from clean_data import clean_text
from get_dates import get_dates
from fetch_tweets import get_tweets
from validate_config import validate_config
from archive_file import archive_data
import os
import json
import sys
import datetime
import crayons
import pandas as pd
sys.path.append('scraper')

# Read in config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Validate config.json and exit if there are any errors
# validate_config returns True if there are no errors
# or a string with the error message if there are errors

if validate_config(config) != True:
    print(crayons.red(f'❌ {validate_config(config)}'))
    print(crayons.red(f'Please fix the errors in config.json and try again.'))
    sys.exit()

# Fetch for current week
start_date, end_date = get_dates(current_week=True)
week, year = datetime.datetime.now().isocalendar(
)[1], datetime.datetime.now().strftime('%Y')

df = pd.DataFrame()

# Get tweets for current week
print(crayons.blue(f' ℹ️ Current week: {week}, year: {year}'))
df = get_tweets(from_date=start_date, to_date=end_date)

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


# Read logger.json
with open('data/logger.json', 'r') as f:
    logger = json.load(f)

# Update logger.json
logger['last_updated'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
logger['last_week'] = week
logger['last_year'] = year

# Write logger.json
with open('data/logger.json', 'w') as f:
    json.dump(logger, f, indent=4)

# If the current week and year are the same as the last week and year
# Then the data is not updated and the file is not archived
if logger['last_week'] == week and logger['last_year'] == year:
    print(crayons.red(
        f'🚫 Data not updated, not archiving file for current week'))
else:
    # If the current week and year are different from the last week and year
    # Then the data is updated and the file is archived
    print(crayons.green(f'📁 Archiving file for current week'))
    archive_data()

# Write CSV File to a new folder in data called current_week
if not os.path.exists('data/current_week'):
    os.makedirs('data/current_week')
df.to_csv(f'data/current_week/data.csv', index=False)
print(crayons.green(
    f'💾 Updated data to data/current_week/data.csv'))

