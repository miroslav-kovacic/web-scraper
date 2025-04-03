from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from datetime import datetime

# Postavi Chrome opcije (blokira detekciju bota)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Pokreće bez GUI-a
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Putanja do ChromeDriver-a
service = Service("chromedriver.exe")  # Zamijeni ako treba

# Pokreni browser
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL eBay oglasa
url = "https://www.ebay.com/itm/266782168480"  # Zamijeni s pravim linkom

# Otvori stranicu
driver.get(url)
time.sleep(3)  # Pričekaj učitavanje

# Dohvati naslov proizvoda
try:
    title = driver.find_element(By.XPATH, '//h1[@class="x-item-title__mainTitle"]').text
except:
    title = "N/A"

# Dohvati cijenu proizvoda
try:
    price = driver.find_element(By.XPATH, '//div[@class="x-price-primary"]/span').text
except:
    price = "N/A"

# Generiraj timestamp za naziv datoteke
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

# Spremi podatke u CSV s jedinstvenim nazivom datoteke
file_name = f"ebay_products_{timestamp}.csv"
data = pd.DataFrame([[title, price, url]], columns=["Title", "Price", "URL"])
data.to_csv(file_name, index=False)

# Ispis rezultata
print(f"Title: {title}")
print(f"Price: {price}")
print(f"Data saved to {file_name}")

# Zatvori browser
driver.quit()
