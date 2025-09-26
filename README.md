# FF-Scraping

A Python project for scraping and analyzing fantasy football data.

## Features

- Scrapes regular season fantasy football data
- Supports single and combined season scraping
- Outputs data for further analysis

## Project Structure

- `reg_season_scraper_single.py`: Scrapes data for a single season
- `reg_season_scraper_range.py`: Scrapes data for all seasons between range from input start and end.
- `reg_season_range_combined.py`: Combines and processes scraped data from seasons in range from input start and end.
- `requirements.txt`: Python dependencies
- `Out of Your League-League-History/`: Example or output data directory taken from input leage name.

## Setup

1. **Clone the repository:**
	 ```sh
	 git clone https://github.com/mfig0321/FF-Scraping.git
	 cd FF-Scraping
	 ```

2. **Create a virtual environment (recommended):**
	 ```sh
	 python3 -m venv .venv
	 source .venv/bin/activate
	 ```

3. **Install dependencies:**
	 ```sh
	 pip install -r requirements.txt
	 ```

## Usage

- To scrape a single season:
	```sh
	python reg_season_scraper_single.py
	```

- To scrape seasons within range:
	```sh
	python reg_season_scraper_range.py
	```

- To combine and process data:
	```sh
	python reg_season_range_combined.py
	```

## Notes

- Update script parameters as needed for your league or data source.
  
  - All Scipts will ask for these input.
    - Will ask for input for league_id.
    - Will ask for input for league_name
    
      - reg_season_scraper_single:
        - Will ask for inout for target season (e.g. 2012)
        - Will output csv with name {season}.csv in Single_Script/Seasons directory
      - reg_season_scraper_range:
        - Will ask for start season year (e.g. 2012)
        - Will ask for end season year (e.g. 2024)
        - Will output a csv for each year in range of start and end years in directory Range_Script directory
      - reg_season_range_combined:
        - Will ask for start season year (e.g. 2012)
        - Will ask for end season year (e.g. 2024)
        - Will out put a single csv with combinbed reg season totals for range of start and end years. In directory Range_Combined_Script
  
## Credits
- github username: sawyercole
- name: Sawyer Cole
  - used his  csvWriting script from https://github.com/sawyercole/FF-Scraping as template
## License

MIT