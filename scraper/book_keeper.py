import json
import crayons
import sys
import datetime
import pandas as pd
import os
sys.path.append('scraper')

from archive_file import archive_data

def logging(config = None, length = None, dates = None):
    week, year = datetime.datetime.now().isocalendar(
)[1], datetime.datetime.now().strftime('%Y')
    # Read logger.json
    with open('data/logger.json', 'r') as f:
        logger = json.load(f)

    # Update logger.json
    logger['last_updated'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger['last_week'] = week
    logger['last_year'] = year
    logger['number_of_tweeks_fetched'] = length
    logger["last_config"]['coords'] = config['coordinates']
    logger["last_config"]['keywords'] = config['search_term']
    logger["last_config"]["date"]["start_date"] = dates['start_date']
    logger["last_config"]["date"]["end_date"] = dates['end_date']
    logger['last_config']['limit'] = config['limit']
    logger['processes']['twitterExtract'] = config['twitterExtract']
    logger['processes']['clean'] = config['clean']
    
    # Convert logger to a CSV file
    # Even the nested JSON keys are converted to individual columns
    logger_df = pd.json_normalize(logger)
    # Fix the column names
    logger_df.columns = logger_df.columns.str.replace(
        'last_config.', '', regex=True).str.replace('processes.', '', regex=True)  
    logger_df.columns = logger_df.columns.str.replace(
        '.', '_', regex=True).str.replace('date.', '', regex=True)  


        
    # Create a CSV file if it does not exist 
    if not os.path.exists('data/fullLog.csv'):
        logger_df.to_csv('data/fullLog.csv', index=False)
    else:
        # If the file exists, append the new data to it
        logger_df.to_csv('data/fullLog.csv', mode='a', header=False, index=False)

    # Write logger.json
    with open('data/logger.json', 'w') as f:
        json.dump(logger, f, indent=4, default=str)

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