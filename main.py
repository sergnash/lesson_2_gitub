import requests
from bs4 import BeautifulSoup


url = 'https://www.irk.ru/weather'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(url, headers=headers, timeout=10)
print(response.status_code)
print(response.text)
