import argparse
from scraper_v1 import scrape_ebay_product, save_to_csv

def main():
    """Main function to execute the scraper."""
    parser = argparse.ArgumentParser(description="Scraper for eBay product price")
    parser.add_argument("url", type=str, help="Usage: python main.py <eBay_product_URL>")
    args = parser.parse_args()

    product_data = scrape_ebay_product(args.url)

    if product_data:
        save_to_csv(product_data)

if __name__ == "__main__":
    main()
