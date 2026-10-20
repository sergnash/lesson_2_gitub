import requests
from bs4 import BeautifulSoup


url = 'https://www.irk.ru/weather'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(url, headers=headers, timeout=10)
if response.status_code == 200:
  {
    soup := BeautifulSoup(response.text, 'html.parser'),
    page_text := soup.get_text(),
    print(page_text)

  }
else:
   print("Ошибка чтения страницы ", response.status_code) 
