# Github Trend Analyzer

A flask app that fetches and scrapes data from the github trending page and displays it sorted by star count. The user can clear previously collected data or continue to fetch more trending repositories whenever the github trending page is updated.

## Features
* Scrape Trending Repositories: Collects data from GitHub's trending page and saves it locally in a JSON file.
* Dynamic Ranking: Sorts repositories by star count for easy navigation.
* Clear Data: Resets the stored data to start fresh.
* Interactive Web Interface: View repository details including name, description, stars, and daily trends.

## Dependencies
The project requires the following Python libraries:
* Flask
* Requests
* BeautifulSoup4

## Usage
1. Clone the repo and install the required libraries:
```
git clone https://github.com/spencerboggs/github-trend-analyzer.git
cd github-trend-analyzer
pip install -r requirements.txt
```
2. Start the app:
```
python app.py
```

The development server will most likely start on http://localhost:5000, if not then check the terminal for the correct url.

Update Data:
* Click the "Update Data" button to scrape the latest trending repositories from GitHub.

View Data:
* The table displays repository names (with clickable links), descriptions, star counts, and stars gained today.
