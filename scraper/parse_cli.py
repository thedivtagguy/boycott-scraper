import argparse

def parse_cli(config):
    # Parse command line arguments
    # CLI arguments are used to specify the week and year, search term, and coordinates
    parser = argparse.ArgumentParser()
    parser.add_argument('--search_term', type=str, help='Search term to look for')
    parser.add_argument('--long', type=float, help='Longitude')
    parser.add_argument('--lat', type=float, help='Latitude')
    parser.add_argument('--radius', type=float, help='Radius to around coordinates')
    parser.add_argument('--limit', type=str, help='Max number of tweets to fetch per search')
    parser.add_argument('--type', type=str, help='Scrape type (custom | weekly | fullYear)')
    parser.add_argument('--start_date', type=str, help='Start date for custom scrape')
    parser.add_argument('--end_date', type=str, help='End date for custom scrape')
    parser.add_argument('--year', type=int, help='Year for full year scrape')
    args = parser.parse_args()

    # If CLI arguments are specified, make changes to config object
    if args.week:
        config['week'] = args.week
    if args.year:
        config['year'] = args.year
    if args.search_term:
        config['search_term'] = args.search_term
    if args.long:
        config['long'] = args.long
    if args.lat:
        config['lat'] = args.lat
    if args.radius:
        config['radius'] = args.radius
    if args.limit:
        config['limit'] = args.limit
    if args.type:
        config['scrape_type'] = args.type
    if args.start_date:
        config['start_date'] = args.start_date
    if args.end_date:
        config['end_date'] = args.end_date
    if args.year:
        config['year'] = args.year

    return config
    