# 😡 Twitter Boycott Tracker

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

## ✂️ Customization 

Don't care about boycotts? I gotchu. This scraper can be easily modified to search for any term you want, no upper limit on the number of results, and can search for tweets from any location.

## 🖨️ Usage

Once downloaded and set up (installation instructions below), there are two ways to use this scraper. You can either run it from the command line, or use the Python script.

### 📋 Script

To run the scraper, simply run the following command:
```bash
    python3 scraper/runner.py
```

All settings, including the term to search for and the number of results to return, are set in the `config.json` file.

```js
{
    "coordinates": {
        "long": 20.5937, // longitude
        "lat": 78.9629,  // latitude
        "radius": 10000  // radius, in kilometers
    },
    "search_term": "boycott", // term to search for
    "clean": "true",          // clean the data? (makes lowercase, removes punctuation, removes stopwords, etc.)
    "twitterExtract": "true", // extract named entities, hashtags, urls, and mentions from the tweets? (slows down the process just a bit)
    "limit": 1000,           // number of results to return per search
    "analysis": "true",      // perform sentiment analysis on the tweets? (slows down the process just a bit)
    "scrape_type": "weekly", // type of search to perform. Options: weekly, fullYear, custom
    "year": 2016,           // year to start searching from, if the above is set to fullYear
    "start_date": "2016-01-01", // date to start searching from, if the above is set to custom
    "end_date": "2016-12-31"    // date to end searching at, if the above is set to custom
}
```

### 🖍️ CLI Access

Script arguments can be passed to the script using the CLI. The following arguments are available:

```js
    --help            show this help message and exit
    --search_term     Search term to use
    --limit           Number of results to return per search
    --radius          Radius to search around, in kilometers
    --lat             Latitude to search around
    --long            Longitude to search around
    --type            Type of search to perform. Options: weekly, fullYear, custom
    --year            Year to start searching from, if the above is set to fullYear
    --start_date      Date to start searching from, if the above is set to custom
    --end_date        Date to end searching at, if the above is set to custom
```

Any of these arguments override the settings in the `config.json` file. 

For example, to search around London (51.5074° N, 0.1278° W) for the term 'monty python' and return 100 results per search, run the following command:

```bash
    python3 scraper/runner.py --search_term "monty python" --limit 100 --lat 51.5074 --long -0.1278
```

If you want to search for the term 'boycott' every week, starting from the current week, but limit to just 5 results per search, run the following command:

```bash
    python3 scraper/runner.py --search_term "boycott" --limit 5 --type weekly
```

## 📁 Data

After each run, the updates of the week are saved in the `data` folder. For the latest data, see the `data/current_week` folder.
Details about the run are logged in `data/logger.json`.

After the first run, the old data is saved in the `data/YEAR` folder. The old data is overwritten. The filename is of the format
    
        tweets-YEAR-WEEK.csv

## 📦 Installation

This project uses Python 3.6. Here's how to get it up and running:

1. Clone the repository:

```bash
git clone https://github.com/thedivtagguy/boycott-scraper.git
```
2. Change into the repository directory:

```bash
cd boycott-scraper
```
3. (Optional) Create and activate a virtual environment. Can be skipped if you don't want to use a virtual environment.

```bash
# create a virtual environment
python -m venv env
# activate the virtual environment (Linux/MacOS)
source env/bin/activate
# activate the virtual environment (Windows)
env/Scripts/activate
```
4. Install the required packages:
```bash
pip install -r requirements.txt
```

Done! You're ready to go. Refer to the Usage section above for more information.

## 🧠 Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## 🧾 Licensing

The code in this project is licensed under MIT license.

## 📮 Contact

If you have any questions, please contact me at [my email](mailto:amanbhargava2001@gmail.com).

