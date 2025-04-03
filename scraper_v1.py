import requests
from bs4 import BeautifulSoup

url  = "https://www.ebay.com/itm/266782168480"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())  # Prikazuje dohvaćeni HTML
else:
    print("Failed to fetch page.")
