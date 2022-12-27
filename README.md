# Twitter Boycott Tracker

There's always something to be outraged about. What is it this week? 

This scraper searches for tweets containing the term 'boycott' and returns 1000 results for each week. It also cleans the data and returns a csv file with the following columns:

- `user`: Contains a JSON object with the user's information. Includes the user's name, screen name, location, description, followers, friends, and favourites count.
- `rawContent`: Contains the raw text of the tweet.
- `created`: Contains the date and time the tweet was created.
- `named_entities`: Contains a comma-separated list of named entities found in the tweet.
- `hashtags`: Contains a comma-separated list of hashtags found in the tweet.
- `urls`: Contains a comma-separated list of urls found in the tweet.
- `mentions`: Contains a comma-separated list of mentions found in the tweet.
- `followers`: Contains the number of followers the user has.

## Usage

To run the scraper, simply run the following command:

    python3 scraper/runner.py

All settings, including the term to search for and the number of results to return, are set in the `config.json` file.

    {
            "coordinates": {
                "long": 20.5937, # Longitude
                "lat": 78.9629,  # Latitude
                "radius": 10000  # Radius in kilometers
            },
            "search_term": "boycott",
            "weekly": "true",    # Search every week, starting from the current week
            "year": "2016",      # Year to start searching from, if the above is set to false
            "week": "1",         # Week to start searching from, if the above is set to false
            "limit": "1000"      # Number of results to return per search
    }

After each run, the updates of the week are saved in the `data` folder. For the latest data, see the `data/current_week` folder.
Details about the run are logged in `data/logger.json`.

After the first run, the old data is saved in the `data/YEAR` folder. The old data is overwritten. The filename is of the format
    
        tweets-YEAR-WEEK.csv

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing

The code in this project is licensed under MIT license.

## Contact

If you have any questions, please contact me at [my email](mailto:amanbhargava2001@gmail.com).

