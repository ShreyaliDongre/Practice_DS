#https://github.com/martj42/international_results
# https://ticker.finology.in/investor/abu-dhabi-investment-authority
# https://ticker.finology.in/investor/abakkus-fund-sunil-singhania
# Scenario using web scraping to get the data from the above links and then using multi-threading to process the data concurrently.

import threading
import requests
from bs4 import BeautifulSoup

urls = ['https://operavps.com/docs/check-installed-package-linux/',
        'https://www.geeksforgeeks.org/installation-guide/beautifulsoup-installation-python/']

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

