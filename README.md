# eBay Product Price Scraper

This is a Python script that scrapes product prices from eBay and saves them into a CSV file.

## Features
- Extracts **product title** and **price** from eBay.
- Saves data into a **CSV file**.
- Simple **command-line interface**.
- Uses **BeautifulSoup** and **requests**.

## Installation

1. Clone the repository:
`git clone https://github.com/yourusername/ebay-scraper.git cd ebay-scraper
`
2. Install dependencies:
`pip install -r requirements.txt`


## Usage

Run the scraper by providing an eBay product URL:
`python main.py "https://www.ebay.com/itm/example-product-url"`


The scraped data will be saved in `output/ebay_prices.csv`.

## Example Output

| Title | Price | URL |
|-------|-------|-----|
| Example Product | $19.99 | https://www.ebay.com/itm/example-product-url |

## Future Improvements
- Support for more e-commerce websites (Amazon, Etsy, etc.).
- Store data in a database instead of CSV.
- Implement a web interface.

## License
This project is licensed under the MIT License - feel free to modify and share.
