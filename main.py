import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

url = 'https://www.irk.ru/weather'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  
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
    if  match: 
          now = datetime.now()
          print('\n','Погода в Иркутске сейчас (',f"{now:%Y-%m-%d %H:%M}",'):', sep='')
          print('температура ', match.group(1), '°', sep='')
          print('ветер ',match.group(2),' м/с', sep='')
          print('влажность ',match.group(3),'%', sep='')
          print('давление ',match.group(4),' мм рт. ст.', sep='')
except requests.exceptions.RequestException as e:
    print("Ошибка чтения страницы:", e)
except Exception as e:
    print("Непредвиденная ошибка:", e)