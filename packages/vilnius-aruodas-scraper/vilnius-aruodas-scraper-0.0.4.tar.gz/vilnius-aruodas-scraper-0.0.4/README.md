# The Aruodas Web-scraper
## Description

This web_scraper is designed to collect the following information for apartments listed on the [Aruodas website](https://en.aruodas.lt/).
* City
* Sub-district
* Description
* Link
* Building number
* Flat number
* Area
* Price per month
* Build year
* Building type
* Heating system
* Energy class
* Nearest kindergarten
* Nearest educational institution
* Nearest stop
* Nearest public transport stop

The scraper has 3 methods:
* scrape - Loops through webpages and scrapes data off the [aruodas.lt](https://en.aruodas.lt/) website.
* to_csv - Used to save the dataframe to csv
* scrape_to_csv - Used to scrape and save the data to csv

### Usage
To use the scaper, pip install the package.
```python
pip install vilnius-aruodas-scraper

from aruodas_scraper import AruodasScraper()

data = AruodasScraper()

# to scrape and data
df = data.scrape(num_houses=100, room_min=1, room_max=3)

# to save scraped data to csv
data.to_csv(df)

# to scrape and save data to csv
data.scrape_to_csv(num_houses=100, room_min=1, room_max=3)

```

## License
The MIT License - Copyright (c) 2021 - Blessing Ehizojie-Philips
