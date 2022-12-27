# This function takes the current data.csv file
# in data/current_week and moves it to 
# The relevant year folder
# Renames it to the relevant week number
# Eg: data/2021/tweets-2021-1.csv

import os
import sys
import datetime
import crayons
import pandas as pd
sys.path.append('scraper')

def archive_data():
    # Get the current week number
    week, year = datetime.datetime.now().isocalendar()[1], datetime.datetime.now().strftime('%Y')

    # If data folder does not exist for the year, create it
    if not os.path.exists(f'data/{year}'):
        os.makedirs(f'data/{year}')

    # Read data/current_week/data.csv
    df = pd.read_csv('data/current_week/data.csv')

    # Write CSV File
    # Name of file is current year and week number
    df.to_csv(f'data/{year}/tweets-{year}-{week}.csv', index=False)

    # Remove data/current_week/data.csv
    os.remove('data/current_week/data.csv')

    print(crayons.green(f'📁 Archived data to data/{year}/tweets-{year}-{week}.csv'))