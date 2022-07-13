import json
import requests
from  datetime import datetime

url = 'http://newsline.kg/getNews.php?limit=30&last_dt=2022-07-04%2007:57:33.933739'
response = requests.get(url)
last_date = datetime.now()
data = json.loads(response.text)
with open('data.json', 'w', encoding ="UTF-8") as file:
   file.write(json.dumps(data['data'], indent=4, ensure_ascii= False))
   print("Успешно записан!")

# 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