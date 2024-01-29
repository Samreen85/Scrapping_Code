# Rightmove Scraper
## Introduction

This Python script utilizes Selenium to scrape property data from the 'Rightmove' website. The primary goal is the extraction of information related to properties listed on Rightmove, generating a dataset that includes details such as address, price, features, description, tenure, nearby stations, council tax, schools, sale price, and price history.

## Installation

1. Clone the repository to your local machine:
* git clone https://github.com/your-username/rightmove-scraper.git

2. Navigate to the project directory: 
* cd rightmove-scraper

3. Ensure you have the latest version of ChromeDriver installed using the following:

* webdriver_manager chrome

## Usage

1. Ensure you have a file named links.json containing the list of Rightmove URLs to be scraped.

2. Run the script:

* python rightmove_scraper.py

The script will iterate through the URLs in links.json, extract property information, and save the data to CSV files (50 URLs per file). The CSV files will be named sequentially as To_1.csv, To_2.csv, and so on.

## Notes:

* The script utilizes headless browsing (--headless option) for faster scraping. You can disable it by modifying the chrome_options in the script if you want to observe the process.

* It is recommended to handle exceptions and edge cases that may arise during scraping. The script currently has basic error handling, but additional improvements may be required based on your specific needs.

* Adjust the sleep durations (time.sleep()) as needed to ensure proper page loading before extracting data.*

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code according to your requirements.