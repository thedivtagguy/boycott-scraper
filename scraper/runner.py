from clean_twitter import clean_tweet
from clean_data import clean_text
from get_dates import get_dates
from fetch_tweets import get_tweets
import os
import sys
import datetime
import crayons
import pandas as pd
sys.path.append('scraper')


# Fetch for current week
start_date, end_date = get_dates(current_week=True)
week, year = datetime.datetime.now().isocalendar(
)[1], datetime.datetime.now().strftime('%Y')

df = pd.DataFrame()

# Check if a file for the current week already exists in data/current_week
# It is possible that the scraper is run multiple times in the same week
# If the file exists, us that file instead of fetching new data

if os.path.exists(f'data/current_week/tweets-{year}-{week}.csv'):
    print(crayons.green(
        f'File for current week already exists, using that file instead of fetching new data'))
    df = pd.read_csv(f'data/current_week/tweets-{year}-{week}.csv')
else:
    # Get tweets for current week
    print(crayons.blue(f' ℹ️ Current week: {week}, year: {year}'))
    df = get_tweets(from_date=start_date, to_date=end_date)

# Clean twitter data
print(crayons.yellow(f'📇 Extracting twitter data...'))
df = clean_tweet(df)

# Clean text in the rawContent column
print(crayons.yellow(f'🧹 Cleaning text...'))
df['rawContent'] = df['rawContent'].apply(clean_text)

# Write CSV File to a new folder in data called current_week
if not os.path.exists('data/current_week'):
    os.makedirs('data/current_week')
df.to_csv(f'data/current_week/tweets-{year}-{week}.csv', index=False)
print(crayons.green(
    f'💾 Updated data to data/current_week/tweets-{year}-{week}.csv'))
