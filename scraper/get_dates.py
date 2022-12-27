# Exports a function that returns a date range
#
# Usage:
#   start_date, end_date = get_dates(year=2021, week_num=1)
#   start_date, end_date = get_dates(current_week=True)
#   start_date, end_date = get_dates(start_date='2021-01-01', end_date='2021-01-31')
#
# Returns:
#   start_date: datetime.date
#   end_date: datetime.date
#
# Raises:
#   ValueError: If invalid combination of arguments is provided
#

import datetime

def get_dates(year=None, week_num=None, current_week=False, start_date=None, end_date=None):
    if year is not None and week_num is not None:
        # Calculate start and end dates for specified year and week number
        start_date = datetime.datetime.strptime(f'{year}-W{week_num}-1', "%Y-W%W-%w").date()
        end_date = datetime.datetime.strptime(f'{year}-W{week_num+1}-1', "%Y-W%W-%w").date()
    
    elif current_week:
        # Calculate start and end dates for current week
        week_num = datetime.datetime.now().isocalendar()[1]
        start_date = datetime.datetime.strptime(f'{datetime.datetime.now().year}-W{week_num-1}-1', "%Y-W%W-%w").date()
        end_date = datetime.datetime.strptime(f'{datetime.datetime.now().year}-W{week_num}-1', "%Y-W%W-%w").date()
    
    elif start_date is not None and end_date is not None:
        # Use provided start and end dates
        pass
    
    else:
        raise ValueError("Invalid combination of arguments")
    return (start_date, end_date)

# Path: scraper\get_tweets.py
