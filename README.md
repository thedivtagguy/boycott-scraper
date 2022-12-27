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
                "long": 20.5937, // Longitude
                "lat": 78.9629,  // Latitude
                "radius": 10000  // Radius in kilometers
            },
            "search_term": "boycott", // Default search term
            "limit": "1000"      // Number of results to return per search. No upper limit!

            // OPTIONAL
            "weekly": "true",    // Search every week, starting from the current week
            "year": "2016",      // Year to start searching from, if the above is set to false
            "week": "1",         // Week to start searching from, if the above is set to false
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
    Change into the repository directory:

cd boycott-scraper

    (Optional) Create and activate a virtual environment. Can be skipped if you don't want to use a virtual environment.

# create a virtual environment
python -m venv env

# activate the virtual environment (Linux/MacOS)
source env/bin/activate

# activate the virtual environment (Windows)
env\Scripts\activate.bat

    Install the required packages:

pip install -r requirements.txt
```

## 🧠 Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## 🧾 Licensing

The code in this project is licensed under MIT license.

## 📮 Contact

If you have any questions, please contact me at [my email](mailto:amanbhargava2001@gmail.com).

