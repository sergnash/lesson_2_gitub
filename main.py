import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.irk.ru/weather'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(url, headers=headers, timeout=10)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text()
    pattern = re.compile( 
        r'([+-]?\d+)(?=°)' 
        r'(?=.*?ветер.*?(\d+)\s*м/с)' 
        r'(?=.*?влажность\s*(\d+)%)' 
        r'(?=.*?давление\s*(\d+))', 
        re.DOTALL | re.IGNORECASE 
    )
    match = re.search(pattern, page_text)
    print(match)
    if  match: 
          print('\n','Погода в Иркутске сейчас:', sep='')
          print('температура ', match.group(1), '°', sep='')
          print('ветер ',match.group(2),' м/с', sep='')
          print('влажность ',match.group(3),'%', sep='')
          print('давление ',match.group(4),' мм рт. ст.', sep='')
else:
   print("Ошибка чтения страницы ", response.status_code) 
