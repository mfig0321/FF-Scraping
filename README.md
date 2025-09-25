# FF-Scraping

A Python project for scraping and analyzing fantasy football data.

## Features

- Scrapes regular season fantasy football data
- Supports single and combined season scraping
- Outputs data for further analysis

## Project Structure

- `reg_season_scrapper_single.py`: Scrapes data for a single season
- `reg_season_scrapper_all.py`: Scrapes data for all seasons
- `reg_season_all_combined.py`: Combines and processes scraped data
- `reg_season_toal.py`: Additional data processing (custom logic)
- `requirements.txt`: Python dependencies
- `Out of Your League-League-History/`: Example or output data directory

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
	python reg_season_scrapper_single.py
	```

- To scrape all seasons:
	```sh
	python reg_season_scrapper_all.py
	```

- To combine and process data:
	```sh
	python reg_season_all_combined.py
	```

## Notes

- Update script parameters as needed for your league or data source.
- Output files will be saved in the project directory or specified folders.

## License

MIT